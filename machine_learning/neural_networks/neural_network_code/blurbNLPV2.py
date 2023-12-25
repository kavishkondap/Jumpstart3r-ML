import tensorflow as tf
import numpy as np
import pandas as pd
# with open ("sarcasm.json", 'r') as f:
#     datastore = json.load (f)
df = pd.read_excel ('dataProcessing.xlsx')
sentences= []
labels = []
# for item in datastore:
for i in range (len (df['Blurbs'])):
    sentences.append (str(df['Blurbs'][i]))
    labels.append (int (df['Success'][i]))

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# sentences = np.asarray (sentencesArr, dtype = str)
# for i, sentence in enumerate (sentencesArr):
#     sentences[i] = sentence

training_size = 20000
training_sentences = sentences [0:training_size]
testing_sentences = sentences [training_size:]
training_labels = labels [0:training_size]
testing_labels = labels [training_size:]

vocab_size = 100000
padding_type = 'post'
trunc_type = 'post'
maxlen = 160

tokenizer = Tokenizer (num_words = vocab_size, oov_token = "<OOV>")
tokenizer.fit_on_texts (training_sentences)
word_index = tokenizer.word_index

training_sequences = tokenizer.texts_to_sequences (training_sentences)
training_padded = pad_sequences(training_sequences, maxlen = maxlen, padding = padding_type, truncating = trunc_type)
testing_sequences = tokenizer.texts_to_sequences (testing_sentences)
testing_padded = pad_sequences(testing_sequences, maxlen = maxlen, padding = padding_type, truncating = trunc_type)

# import numpy as np
training_padded = np.array(training_padded)
training_labels = np.array(training_labels)
testing_padded = np.array(testing_padded)
testing_labels = np.array(testing_labels)
print ("LABELS: ", training_labels)
# print (padded[0])
# print (padded.shape)
embedding_dim = 16
model = tf.keras.Sequential ([
    tf.keras.layers.Embedding (vocab_size, embedding_dim, input_length=maxlen),
    tf.keras.layers.GlobalAveragePooling1D (),
    tf.keras.layers.Dense (24, activation = 'relu'),
    tf.keras.layers.Dense (1, activation = 'sigmoid')
])

model.compile (loss = 'binary_crossentropy', optimizer='adam', metrics = ['accuracy'])

num_epochs = 30
history = model.fit (training_padded, training_labels, epochs = num_epochs, validation_data=(testing_padded, testing_labels), verbose = 2)
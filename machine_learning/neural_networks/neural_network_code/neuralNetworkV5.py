import os
# from tabnanny import verbose
# from pkg_resources import add_activation_listener
os.environ ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import layers, Model
from tensorflow.keras.layers.experimental import preprocessing
from tensorflow.keras.layers import LSTM, Bidirectional, Dense, concatenate, Embedding, Input
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def get_nlp_data (training_size):
    df = pd.read_excel ('machineLearningData.xlsx')
    sentences= []
    labels = []
    # for item in datastore:
    for i in range (len (df['titles'])):
        sentences.append (str(df['titles'][i]))
        labels.append (int (df['successes'][i]))
    print ("SENTENCES LEN", len (sentences))
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
    # word_index = tokenizer.word_index

    training_sequences = tokenizer.texts_to_sequences (training_sentences)
    training_padded = pad_sequences(training_sequences, maxlen = maxlen, padding = padding_type, truncating = trunc_type)
    testing_sequences = tokenizer.texts_to_sequences (testing_sentences)
    testing_padded = pad_sequences(testing_sequences, maxlen = maxlen, padding = padding_type, truncating = trunc_type)

    # import numpy as np
    training_padded = np.array(training_padded)
    training_labels = np.array(training_labels)
    testing_padded = np.array(testing_padded)
    testing_labels = np.array(testing_labels)
    # print ("TP", training_padded)
    return [training_padded, training_labels, testing_padded, testing_labels]

data = pd.read_excel ('machineLearningData.xlsx')
labels= np.array (data.pop ('successes'))
#Data not being used for ML model
data.pop ("ids")
data.pop ("urls")
data.pop ("titles")
data.pop ("blurbs")
data.pop ("top_media")
data.pop ("bottom_media")

data = np.array (data)
print ("data shape", data.shape)
print ("Labels shape", labels.shape)
numRows, numCols = data.shape
training_size = int(numRows * 0.8)
print ('training_size', training_size)

training_data = data [0:training_size]
training_labels = labels [0:training_size]
print ('training data', training_data.shape)
print ('training_labels', training_labels.shape)
testing_data = data [training_size:]
testing_labels = labels [training_size:]

val_size = int (training_size*0.2)
print ('val_size', val_size)
val_data = training_data [0:val_size]
training_data = training_data [val_size:]
print ('training_data _post_Val', training_data.shape)
val_labels = training_labels [0:val_size]
training_labels = training_labels [val_size:]
print ('training_labels post val', training_labels)

nlp_data = get_nlp_data(training_size)

training_nlp_data = np.array (nlp_data [0])
print ("TRAINING NLP DATA", training_nlp_data.shape)
training_nlp_labels = nlp_data [1]
testing_nlp_data = np.array (nlp_data[2])
testing_nlp_labels = nlp_data [3]

val_nlp_data = training_nlp_data [0:val_size]
training_nlp_data = training_nlp_data [val_size:]
val_nlp_labels = training_nlp_data [0:val_size]
training_nlp_labels = training_nlp_data [val_size:]
# print (training_nlp_data)
# normalizer = preprocessing.Normalization()
# normalizer.adapt(np.array(training_data))
voc_size = (training_nlp_data.max ()+1).astype ('int64')


numerical_model = Input (shape = (5))
nlp_model = Input (shape =(160)) #160 is maxlen of words
emb = Embedding (input_dim = voc_size , output_dim = 16, input_length=numCols)(nlp_model)
nlp_out = Bidirectional (LSTM (128))(emb)
concat = concatenate ([nlp_out, numerical_model])
classifier = Dense (64, activation = 'relu')(concat)
classifier2 = Dense (64, activation = 'relu')(concat)
output = Dense (1, activation = 'sigmoid')(classifier2)
model = Model (inputs=[nlp_model, numerical_model], outputs=[output])

loss = keras.losses.BinaryCrossentropy  (from_logits=False)
optim = keras.optimizers.Adam(learning_rate=0.005)
metrics = ["accuracy"]

model.compile (loss=loss, optimizer = optim, metrics=metrics)
batch_size = 64
epochs = 100

print ("training data: ", training_data.shape)
print ('nlp_data: ', training_nlp_data.shape)
print ("training_labels", training_labels.shape)
model.fit ([training_nlp_data, training_data], training_labels, batch_size = batch_size, epochs = epochs, shuffle = True, validation_data = ([val_nlp_data, val_data], val_labels), verbose = 2)
print ("EVAL")
model.evaluate (testing_data, testing_labels, batch_size=batch_size, verbose = 2)
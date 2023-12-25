from itertools import count
import pandas as pd
import numpy as np
import re
import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# --- DATA PROCESSING ---
data = pd.read_excel ('KickstarterData.xlsx')

success = np.array (data['success'])
lemmatizer = WordNetLemmatizer ()

blurbs = data ['blurb'].astype ('str')

for i in range (len(blurbs)):
    str = blurbs[i]
    str = str.strip () #remove whitespace
    str = str.lower () #make lowercase
    str = re.sub (r'[^\w\s]', '', str) #remove ,.!? etc
    str = re.sub (' +', ' ', str) #get rid of random double spaces that are there for some reason
    words = str.split (' ') 
    newStr = ''
    for word in words:
        newStr += lemmatizer.lemmatize (word) + ' ' #lemmatizing
    blurbs [i] = newStr #final refined string

# --- MACHINE LEARNING ---

vocab_size = 10000
embedding_dim = 16
max_length = 100
oov_tok = "<OOV>"
trunc_type='post'
padding_type='post'
training_size = 22000
countNone = 0
for blurb in blurbs:
    if (blurb == None or blurb == ''):
        countNone+=1

print ("COUNT NONE: ", countNone)
training_blurbs = blurbs [0:training_size]
testing_blurbs = blurbs [training_size:]
training_labels = success [0:training_size]
testing_labels = success [training_size:]

tokenizer = Tokenizer (oov_token=oov_tok, num_words = vocab_size)
tokenizer.fit_on_texts (training_blurbs)

word_index = tokenizer.word_index

training_sequences = tokenizer.texts_to_sequences (training_blurbs)
training_padded = pad_sequences (training_sequences, maxlen = max_length, padding = padding_type, truncating = trunc_type)

testing_sequences = tokenizer.texts_to_sequences (testing_blurbs)
testing_padded = pad_sequences (testing_sequences, maxlen = max_length, padding = padding_type, truncating = trunc_type)

#padding everything
training_padded = np.array(training_padded, dtype = np.float64)
training_labels = np.array(training_labels, dtype = np.float64)

validation_length = int (training_padded.shape [0] * 0.2)

validation_padded = training_padded[0:validation_length]
validation_labels = training_labels[0:validation_length]

training_padded = training_padded [validation_length:]
training_labels = training_labels [validation_length:]


testing_padded = np.array(testing_padded, dtype = np.float64)
testing_labels = np.array(testing_labels, dtype = np.float64)

model = tf.keras.Sequential ([ #fun model stuff
    tf.keras.layers.Embedding (vocab_size, embedding_dim, input_length = max_length),
    tf.keras.layers.GlobalAveragePooling1D (),
    tf.keras.layers.Dense (24, activation = 'relu'),
    # tf.keras.layers.Dense (64, activation = 'relu'),
    tf.keras.layers.Dense (1, activation = 'sigmoid')
])
print ("MODEL SUMMARY")
model.summary()
model.compile (loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
num_epochs = 30
batch_size = 64
#fitting to model
model.fit (training_padded, training_labels, batch_size = batch_size, epochs = num_epochs, validation_data = (validation_padded, validation_labels), verbose= 2)
model.evaluate (testing_padded, testing_labels, verbose = 2)

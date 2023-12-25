import os
from typing import Concatenate
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

def get_nlp_data ():
    df = pd.read_excel ('dataProcessing.xlsx')
    sentences= []
    labels = []
    # for item in datastore:
    for i in range (len (df['Blurbs'])):
        sentences.append (str(df['Blurbs'][i]))
        labels.append (int (df['Success'][i]))
    
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

    return [training_padded, training_labels, testing_padded, testing_labels]

data = pd.read_excel ('dataProcessing.xlsx')
labels= np.array (data.pop ('Success'))
blurbs = data.pop ('Blurbs')
latitude = data.pop ('Latitude')
longitude = data.pop ('Longitude')
backers = data.pop ('Backers')
data = np.array (data, dtype = np.float64)
nlp_data = get_nlp_data()

training_nlp_data = np.array (nlp_data [0])
training_nlp_labels = nlp_data [1]
testing_nlp_data = np.array (nlp_data[2])
# for i in range (len (training_nlp_data)):
#     training_nlp_data[i] = (training_nlp_data[i]+[1])
testing_nlp_labels = nlp_data [3]

numRows, numCols = data.shape
training_size = 20000
# print (data.shape)
# print (training_size)

training_data = data [0:training_size]
# print (training_data.size)
training_labels = labels [0:training_size]
print (training_data)
print (training_labels)
testing_data = data [training_size:data.size]
testing_labels = labels [training_size:data.size]

numRows, numCols = np.array (training_data).shape
training_size = int(numRows * 0.8)
# print (data.shape)
# print (training_size)
val_data = training_data [0:training_size]
training_data = training_data [training_size:]
# print (training_data.size)
val_labels = training_labels [0:training_size]
training_labels = training_labels [training_size:]

val_nlp_data = training_nlp_data [0:training_size]
training_nlp_data = training_nlp_data [training_size:]
val_nlp_labels = training_nlp_data [0:training_size]
training_nlp_labels = training_nlp_data [training_size:]
# print (testing_data)
# print (testing_labels)
normalizer = preprocessing.Normalization()

normalizer.adapt(np.array(training_data))
voc_size = (training_nlp_data.max ()+1).astype ('int64')
# for i in range (6):
#     plt.subplot (2, 3, i+1)
#     plt.imshow (x_train[i], cmap = 'gray')
# plt.show()
print ("NUM COLS: ", numCols)
numerical_model = Input (shape=(6,))
nlp_model = Input (shape =(160))
emb = Embedding (input_dim = voc_size , output_dim = 16, input_length=numCols)(nlp_model)
nlp_out = Bidirectional (LSTM (128))(emb)
concat = concatenate ([nlp_out, numerical_model])
classifier = Dense (64, activation = 'relu')(concat)
classifier2 = Dense (64, activation = 'relu')(concat)
output = Dense (1, activation = 'sigmoid')(classifier2)
model = Model (inputs=[nlp_model, numerical_model], outputs=[output])

# model = keras.models.Sequential ([
#     normalizer,
#     keras.layers.Dense(64, activation = 'relu'),
#     keras.layers.Dense(64, activation = 'relu'), # amount can change
#     keras.layers.Dense (1),
# ])

# print (model.summary())

loss = keras.losses.BinaryCrossentropy  (from_logits=False)
optim = keras.optimizers.Adam(lr=0.005)
metrics = ["accuracy"]

model.compile (loss=loss, optimizer = optim, metrics=metrics)
batch_size = 64
epochs = 30

# checkpoint_path = "training_1/cp.ckpt"
# checkpoint_dir = os.path.dirname(checkpoint_path)
# cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
#                                                  save_weights_only=True,
#                                                  verbose=1)

print ("training data: ", training_data)
print ('nlp_data: ', training_nlp_data)
model.fit ([training_nlp_data, training_data], training_labels, batch_size = batch_size, epochs = epochs, shuffle = True, validation_data = ([val_nlp_data, val_data], val_labels), verbose = 2)
print ("EVAL")
model.evaluate (testing_data, testing_labels, batch_size=batch_size, verbose = 2)
print ("CUSTOM")
customTestData = np.array ([[1, 2, 99, 11, 106381.58, 12]])
customTestLabel = np.array ([1])
model.evaluate (customTestData, customTestLabel, verbose = 2)
# probability = keras.models.Sequential ([
#     model,
#     keras.layers.Softmax()
# ])

# predictions = probability(testing_data)
# pred0 = predictions [0]
# print (pred0)
# label0 = np.argmax (pred0)
# print (label0)
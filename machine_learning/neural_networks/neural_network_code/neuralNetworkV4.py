import os
# from tabnanny import verbose
# from pkg_resources import add_activation_listener
os.environ ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

data = pd.read_excel ('machineLearningData.xlsx')
labels= np.array (data.pop ('successes'))
# print (labels)

#Data not being used for ML model
data.pop ("ids")
data.pop ("urls")
data.pop ("titles")
data.pop ("blurbs")
# for i, blurb in enumerate (data['blurbs']):
#     data['blurbs'][i] = len (str (blurb))
# for i, title in enumerate (data['titles']):
#     data['titles'][i] = len (str (title))
data.pop ("top_media")
data.pop ("bottom_media")
# print (data)

data = np.array (data)
numRows, numCols = data.shape
training_size = int(numRows * 0.8)

training_data = data [0:training_size]
training_labels = labels [0:training_size]
print (training_data.shape)
print (training_labels)
testing_data = data [training_size:data.size]
testing_labels = labels [training_size:data.size]


normalizer = preprocessing.Normalization()

normalizer.adapt(np.array(training_data))

model = keras.models.Sequential ([
    normalizer,
    keras.layers.Dense(256, activation = 'relu'),
    keras.layers.Dense(256, activation = 'relu'),
    keras.layers.Dense(256, activation = 'relu'), # amount can change
    keras.layers.Dense (1, activation = 'sigmoid'),
])

print (model.summary())

loss = keras.losses.BinaryCrossentropy  ()
optim = keras.optimizers.Adam(learning_rate=0.0005)
metrics = ["accuracy"]

model.compile (loss=loss, optimizer = optim, metrics=metrics)
batch_size = 4
epochs = 20

numRows, numCols = np.array (training_data).shape
training_size = int(numRows * 0.8)
val_data = training_data [0:training_size]
training_data = data [training_size:]
val_labels = training_labels [0:training_size]
training_labels = labels [training_size:]
print ("TRAINING LABELS: ", training_labels)
model.fit (training_data, training_labels, batch_size = batch_size, epochs = epochs, shuffle = True, validation_data = (val_data, val_labels), verbose = 2)
print ("EVAL")
model.evaluate (testing_data, testing_labels, batch_size=batch_size, verbose = 2)

# model.save ('NN_v7')
# model.save ('NN_v6.h5')
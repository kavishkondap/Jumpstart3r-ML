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

data = pd.read_excel ('dataProcessing2.xlsx')
labels= np.array (data.pop ('Success'))
data.pop ('Amount Raised')
# blurbs = data.pop ('Blurbs')
for i, blurb in enumerate (data['Blurbs']):
    data['Blurbs'][i] = len (str (blurb))
for i, title in enumerate (data['Title']):
    data['Title'][i] = len (str (title))
# latitude = data.pop ('Latitude')
# longitude = data.pop ('Longitude')
backers = data.pop ('Backers')
comments = data.pop ('Comments')
data.pop ('Latitude')
data.pop ('Longitude')
data = np.array (data, dtype = np.float64)
numRows, numCols = data.shape
training_size = int(numRows * 0.8)
# print (data.shape)
# print (training_size)

training_data = data [0:training_size]
# print (training_data.size)
training_labels = labels [0:training_size]
print (training_data)
print (training_labels)
testing_data = data [training_size:data.size]
testing_labels = labels [training_size:data.size]
# print (testing_data)
# print (testing_labels)
normalizer = preprocessing.Normalization()

normalizer.adapt(np.array(training_data))

# for i in range (6):
#     plt.subplot (2, 3, i+1)
#     plt.imshow (x_train[i], cmap = 'gray')
# plt.show()

model = keras.models.Sequential ([
    normalizer,
    keras.layers.Dense(64, activation = 'relu'),
    keras.layers.Dense(64, activation = 'relu'),
    keras.layers.Dense(64, activation = 'relu'), # amount can change
    keras.layers.Dense (1),
])

print (model.summary())

loss = keras.losses.BinaryCrossentropy  (from_logits=True)
optim = keras.optimizers.Adam(learning_rate=0.0005)
metrics = ["accuracy"]

model.compile (loss=loss, optimizer = optim, metrics=metrics)
batch_size = 4
epochs = 20

numRows, numCols = np.array (training_data).shape
training_size = int(numRows * 0.8)
# print (data.shape)
# print (training_size)
val_data = training_data [0:training_size]
training_data = data [training_size:]
# print (training_data.size)
val_labels = training_labels [0:training_size]
training_labels = labels [training_size:]
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
model.fit (training_data, training_labels, batch_size = batch_size, epochs = epochs, shuffle = True, validation_data = (val_data, val_labels), verbose = 2, callbacks= [cp_callback])
print ("EVAL")
model.evaluate (testing_data, testing_labels, batch_size=batch_size, verbose = 2)
# print ("CUSTOM")
# customTestData = np.array ([[1, 2, 99, 11, 106381.58, 12]])
# customTestLabel = np.array ([1])
# model.evaluate (customTestData, customTestLabel, verbose = 2)
# probability = keras.models.Sequential ([
#     model,
#     keras.layers.Softmax()
# ])

# predictions = probability(testing_data)
# pred0 = predictions [0]
# print (pred0)
# label0 = np.argmax (pred0)
# print (label0)
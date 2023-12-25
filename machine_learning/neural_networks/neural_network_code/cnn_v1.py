import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

data = pd.read_excel('machineLearningData5.xlsx')
labels = np.array(data.pop('successes'))

data.pop("ids")
data.pop("urls")
titles = data.pop("titles")
blurbs = data.pop("blurbs")
data = np.array(data)

numRows, numCols = data.shape
training_size = int(numRows * 0.8)

training_data = data[0:training_size]
training_labels = labels[0:training_size]
testing_data = data[training_size:data.size]
testing_labels = labels[training_size:data.size]

# Reshape the data for convolutional neural network
training_data = training_data.reshape((-1, numCols, 1))
testing_data = testing_data.reshape((-1, numCols, 1))

model = keras.models.Sequential([
    preprocessing.Normalization(),
    layers.Conv1D(32, kernel_size=3, activation='relu'),
    layers.MaxPooling1D(pool_size=2),
    layers.Conv1D(64, kernel_size=3, activation='relu'),
    layers.MaxPooling1D(pool_size=2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])

loss = keras.losses.BinaryCrossentropy()
optim = keras.optimizers.Adam(learning_rate=0.005)
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optim, metrics=metrics)
batch_size = 4
epochs = 100

model.build(input_shape=(None, numCols, 1))  # Build the model

print(model.summary())

model.fit(training_data, training_labels, batch_size=batch_size, epochs=epochs, shuffle=True, verbose=2)
model.evaluate(testing_data, testing_labels, batch_size=batch_size, verbose=2)

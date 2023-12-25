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

normalizer = preprocessing.Normalization()
normalizer.adapt(np.array(training_data))

model = keras.models.Sequential([
    normalizer,
    layers.Embedding(input_dim=numCols, output_dim=64),  # Embedding layer for sequence data
    layers.GRU(64),  # GRU layer for sequence modeling
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])

print(model.summary())

loss = keras.losses.BinaryCrossentropy()
optim = keras.optimizers.Adam(learning_rate=0.005)
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optim, metrics=metrics)
batch_size = 4
epochs = 100

val_size = int(training_size * 0.2)
val_data = training_data[:val_size]
val_labels = training_labels[:val_size]
training_data = training_data[val_size:]
training_labels = training_labels[val_size:]

model.fit(
    training_data,
    training_labels,
    batch_size=batch_size,
    epochs=epochs,
    shuffle=True,
    validation_data=(val_data, val_labels),
    verbose=2
)

model.evaluate(testing_data, testing_labels, batch_size=batch_size, verbose=2)

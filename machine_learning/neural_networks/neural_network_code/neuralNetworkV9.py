# now using measures to prevent overfitting
import os
# from tabnanny import verbose
# from pkg_resources import add_activation_listener
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

data = pd.read_excel('machineLearningData6.xlsx')
# print (data)
labels = np.array(data.pop('successes'))
# print (labels)

# Data not being used for ML model
data.pop("ids")
data.pop("urls")
titles = data.pop("titles")
blurbs = data.pop("blurbs")
print(data.keys())
data = np.array(data)
print(data.shape)
numRows, numCols = data.shape
training_size = int(numRows * 0.8)

training_data = data[0:training_size]
training_labels = labels[0:training_size]
print(training_data.shape)
print(training_labels)
testing_data = data[training_size:data.size]
testing_labels = labels[training_size:data.size]

normalizer = preprocessing.Normalization()
normalizer.adapt(np.array(training_data))

model = keras.models.Sequential([
    normalizer,
    keras.layers.Dense(128, activation='relu'),
    # keras.layers.Dropout(0.001),  # Dropout layer to reduce overfitting
    keras.layers.Dense(128, activation='relu'),
    # keras.layers.Dropout(0.001),  # Dropout layer to reduce overfitting
    keras.layers.Dense(64, activation='relu'),
    # keras.layers.Dropout(0.001),  # Dropout layer to reduce overfitting
    keras.layers.Dense(1, activation='sigmoid'),
])

print(model.summary())

loss = keras.losses.BinaryCrossentropy()
optim = keras.optimizers.Adam(learning_rate=0.01)
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optim, metrics=metrics)
batch_size = 256
epochs = 100

numRows, numCols = np.array(training_data).shape
training_size = int(numRows * 0.8)
val_data = training_data[0:training_size]
training_data = data[training_size:]
val_labels = training_labels[0:training_size]
training_labels = labels[training_size:]
print("TRAINING LABELS: ", training_labels)

# Add EarlyStopping to prevent overfitting
early_stopping = keras.callbacks.EarlyStopping(
    monitor='val_loss', patience=50, restore_best_weights=True
)

model.fit(
    training_data, training_labels, batch_size=batch_size, epochs=epochs,
    shuffle=True, validation_data=(val_data, val_labels),
    callbacks=[early_stopping], verbose=2
)

print("EVAL")
model.evaluate(testing_data, testing_labels, batch_size=batch_size, verbose=2)

# model.save('NN_v10')
# model.save('NN_v6.h5')

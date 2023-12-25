import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

data = pd.read_excel('machineLearningData8.xlsx')
labels = np.array(data.pop('successes'))
data.pop("ids")
data.pop("urls")
titles = data.pop("titles")
blurbs = data.pop("blurbs")
data = np.array(data)
data_labels = list(zip(data, labels))
np.random.shuffle(data_labels)
data, labels = zip(*data_labels)
data = np.array(data)
labels = np.array(labels)

num_rows, num_cols = data.shape
training_size = int(num_rows * 0.8)

training_data = data[:training_size]
training_labels = labels[:training_size]
testing_data = data[training_size:]
testing_labels = labels[training_size:]

normalizer = preprocessing.Normalization()
normalizer.adapt(np.array(training_data))

model = keras.models.Sequential([
    normalizer,
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.1),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.1),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.1),
    keras.layers.Dense(1, activation='sigmoid'),
])

loss = keras.losses.BinaryCrossentropy()
optim = keras.optimizers.Adam(learning_rate=0.001)
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optim, metrics=metrics)

batch_size = 256
epochs = 500

history = model.fit(
    training_data,
    training_labels,
    batch_size=batch_size,
    epochs=epochs,
    shuffle=True,
    validation_split=0.2,  # Splitting a validation set from the training data
    verbose=2
)

# Plotting the training and validation accuracy over epochs
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plotting the training and validation loss over epochs
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

print("EVAL")
model.evaluate(testing_data, testing_labels, batch_size=batch_size, verbose=2)

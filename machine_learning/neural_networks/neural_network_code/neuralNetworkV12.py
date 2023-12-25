import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

data = pd.read_excel('machineLearningData16.xlsx')
labels = np.array(data.pop('successes'))
data.pop("ids")
data.pop("urls")
data.pop ('locations')
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

num_networks = 5  # Number of individual neural network models in the ensemble

models = []  # List to store individual models

for _ in range(num_networks):
    model = keras.models.Sequential([
        normalizer,
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(1, activation='sigmoid'),
    ])
    
    loss = keras.losses.BinaryCrossentropy()
    optim = keras.optimizers.Adam(learning_rate=0.01)
    metrics = ["accuracy"]
    
    model.compile(loss=loss, optimizer=optim, metrics=metrics)
    models.append(model)

batch_size = 100
epochs = 100

ensemble_predictions = []  # List to store predictions from individual models

for model in models:
    history = model.fit(
        training_data,
        training_labels,
        batch_size=batch_size,
        epochs=epochs,
        shuffle=True,
        validation_split=0.2,
        verbose=2
    )
    
    # Collect predictions on testing data from each individual model
    predictions = model.predict(testing_data)
    ensemble_predictions.append(predictions)

ensemble_predictions = np.array(ensemble_predictions)
ensemble_predictions = np.round(np.mean(ensemble_predictions, axis=0))  # Aggregate predictions by taking the mean and rounding to 0 or 1
print (ensemble_predictions)
print (testing_labels)
correct = 0
incorrect = 0
for i in range (len (ensemble_predictions)):
    if (ensemble_predictions[i]==testing_labels[i]):
        correct+=1
    else:
        incorrect+=1
print ("Accuracy:", correct/(correct+incorrect))
ensemble_accuracy = np.mean(ensemble_predictions == testing_labels)  # Calculate ensemble accuracy

print("Ensemble Accuracy:", ensemble_accuracy)

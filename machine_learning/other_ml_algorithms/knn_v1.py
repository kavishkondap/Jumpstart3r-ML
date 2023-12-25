import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

data = pd.read_excel('machineLearningData6.xlsx')

# Extract features and labels
labels = np.array(data.pop('successes'))
data.pop("ids")
data.pop("urls")
data.pop("titles")
data.pop("blurbs")
data = np.array(data)

# Normalize the data
scaler = StandardScaler()
scaler.fit(data)
normalized_data = scaler.transform(data)

# Split the data into training and testing sets
training_size = int(data.shape[0] * 0.8)
training_data = normalized_data[:training_size]
training_labels = labels[:training_size]
testing_data = normalized_data[training_size:]
testing_labels = labels[training_size:]

# Train the k-nearest neighbors algorithm
k = 5  # number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(training_data, training_labels)

# Evaluate the model
accuracy = knn.score(testing_data, testing_labels)
print("Accuracy:", accuracy)

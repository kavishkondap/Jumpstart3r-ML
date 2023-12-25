import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

data = pd.read_excel('machineLearningData5.xlsx')
labels = np.array(data.pop('successes'))
data.pop("ids")
data.pop("urls")
titles = data.pop("titles")
blurbs = data.pop("blurbs")
data = np.array(data)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

training_data, testing_data, training_labels, testing_labels = train_test_split(scaled_data, labels, test_size=0.2, random_state=42)

svm_model = SVC(kernel='rbf')
svm_model.fit(training_data, training_labels)

accuracy = svm_model.score(testing_data, testing_labels)
print("Accuracy:", accuracy)

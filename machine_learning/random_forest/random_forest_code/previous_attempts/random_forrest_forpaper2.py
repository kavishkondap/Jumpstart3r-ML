import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import PartialDependenceDisplay, partial_dependence
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Set the style
# plt.style.use('fivethirtyeight')

data = pd.read_excel('machineLearningData14 graph.xlsx')
labels = np.array(data.pop('successes'))

# Data not being used for ML model
data.pop("ids")
data.pop("urls")
data.pop('locations')
data.pop ('title_keywords')
data.pop ('blurb_keywords')
titles = data.pop("titles")
blurbs = data.pop("blurbs")

data['Media Type'] -= 1

X, x_val, y, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)
var_columns = [c for c in data]

model_rf = RandomForestClassifier()
model_rf.fit(X, y)
print(model_rf.feature_importances_)

print('score', model_rf.score(x_val, y_val))

df_var_imp = pd.DataFrame({'Variable': var_columns,
                           'Importance': model_rf.feature_importances_}) \
                .sort_values(by='Importance', ascending=False) \
                .reset_index(drop=True)

# Customize the bar plot
fig, ax = plt.subplots(figsize=(20, 12))
sorted = df_var_imp.sort_values('Importance')
hbars = ax.barh(list(sorted['Variable']), list(sorted['Importance']))
# ax.set_title('Feature Importance', fontname='Times New Roman')
ax.set_xlabel('Relative Importance', fontname='Times New Roman', fontsize=15)
ax.set_ylabel('Variable', fontname='Times New Roman', fontsize=15)
vals = list(df_var_imp.sort_values('Importance')['Importance'])
print(vals)
print(type(hbars))
ax.bar_label(hbars, fmt='%.4f', fontname='Times New Roman', fontsize=15)
# Rotate x-axis labels and adjust figure size for wrapped text
plt.yticks(rotation='horizontal', wrap=True, fontname='Times New Roman', fontsize=12)
plt.xscale('log')
plt.tick_params(axis='x', which='minor')
plt.xticks(fontname='Times New Roman', fontsize=15)

plt.show()

# Feature for which we want to perform bootstrapping and find the maximum value with uncertainty
selected_feature = 'Number of Updates'
selected_feature_index = var_columns.index(selected_feature)

# Number of bootstrap iterations
num_iterations = 2

# Arrays to store maximum values from each iteration
max_values = []

for _ in range(num_iterations):
    # Randomly resample with replacement to create a new dataset
    indices = np.random.choice(len(X), len(X), replace=True)
    resampled_X = X.iloc[indices]

    # Compute PDP data for the resampled dataset and the selected feature
    pdp_data, _ = partial_dependence(model_rf, resampled_X, features=[selected_feature_index])

    # Extract the feature values and partial dependence values from the pdp_data
    feature_values = pdp_data[0][0]
    partial_dependence_values = pdp_data[1][0]

    # Find the maximum value and its index in the partial dependence values
    max_index = np.argmax(partial_dependence_values)
    max_value = partial_dependence_values[max_index]
    max_values.append(max_value)  # Append the maximum value to the list

# Calculate the uncertainty as the standard deviation of the maximum values
uncertainty = np.std(max_values)

# Find the maximum value and its index in the original partial dependence values
pdp_data, _ = partial_dependence(model_rf, X, features=[selected_feature_index])
feature_values = pdp_data[0][0]
partial_dependence_values = pdp_data[1][0]
max_index = np.argmax(partial_dependence_values)
max_value = partial_dependence_values[max_index]
max_feature_value = feature_values[max_index]

print(f"The maximum value in the PDP graph for {selected_feature} is: {max_value:.2f}")
print(f"It occurs at {selected_feature} = {max_feature_value:.2f}")
print(f"Uncertainty on the maximum value: {uncertainty:.2f}")

fig, ax = plt.subplots(figsize=(6, 4), sharey=True, constrained_layout=True)

features_info = {
    "features": [selected_feature],
    "kind": "both",
    "centered": True,
}

display = PartialDependenceDisplay.from_estimator(
    model_rf,
    X,
    **features_info,
    ax=ax,
    n_jobs=-1,
    random_state=42,
    pd_line_kw={"color": "black"},
)
_ = display.figure_.suptitle(f"ICE and PDP representations for {selected_feature}", fontsize=16)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import PartialDependenceDisplay, partial_dependence
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import joblib

# Set the font family to Times New Roman for matplotlib
import matplotlib as mpl
mpl.rc('font', family='Times New Roman')

# Load data from an Excel file
data = pd.read_excel('machineLearningData14 graph.xlsx')

# Extract labels from the data
labels = np.array(data.pop('successes'))

# Remove unnecessary columns from the data
data.drop(["ids", "urls", "locations", "title_keywords", "blurb_keywords"], axis=1, inplace=True)

# Separate titles and blurbs from the data
titles = data.pop("titles")
blurbs = data.pop("blurbs")

# Adjust the 'Media Type' column
data['Media Type'] -= 1

# Split the data into training and validation sets
X, x_val, y, y_val = train_test_split(data, labels, test_size=0.2)

# Create a Random Forest classifier and train it on the data
model_rf = RandomForestClassifier()
model_rf.fit(X, y)

# Print the model's accuracy on the validation set
print('Validation Score:', model_rf.score(x_val, y_val))

# Perform cross-validation and print the results
cross_val = cross_val_score(model_rf, x_val, y_val, cv=5, scoring='roc_auc')
print('Cross-Validation Scores:', cross_val)

# Create a DataFrame for feature importances and sort it
df_var_imp = pd.DataFrame({'Variable': data.columns, 'Importance': model_rf.feature_importances_})
df_var_imp = df_var_imp.sort_values(by='Importance', ascending=False).reset_index(drop=True)

# Create a bar plot for feature importances
fig, ax = plt.subplots(figsize=(17, 15))
plt.subplots_adjust(left=0.18)
hbars = ax.barh(df_var_imp['Variable'], df_var_imp['Importance'])
ax.set_xlabel('Relative Importance', fontname='Times New Roman', fontsize=30)
ax.bar_label(hbars, fmt='%.4f', fontname='Times New Roman', fontsize=22)
plt.yticks(rotation='horizontal', wrap=True, fontname='Times New Roman', fontsize=25)
plt.xscale('log')
plt.tick_params(axis='x', which='minor')
plt.xticks(fontname='Times New Roman', fontsize=30)
plt.show()

# Create Partial Dependence Plots for each feature
feature_options = list(data.keys())
for feature in feature_options:
    fig, ax = plt.subplots(figsize=(18, 12), sharey=True, constrained_layout=True)
    features_info = {
        "features": [str(feature)],
        "kind": "both",
        "centered": True,
    }
    common_params = {
        'n_jobs': -1,
        'random_state': 42,
    }
    display = PartialDependenceDisplay.from_estimator(model_rf, X, **features_info, ax=ax, **common_params, pd_line_kw={"color": "black"})
    _ = display.figure_.suptitle(f"ICE and PDP representations for {features_info['features'][0]}", fontsize=25)
    plt.legend(fontsize=35)
    ax.xaxis.label.set_fontsize(25)
    ax.yaxis.label.set_fontsize(25)
    plt.xticks(fontname='Times New Roman', fontsize=15)
    plt.yticks(fontname='Times New Roman', fontsize=15)
    plt.savefig('PDP_' + str(feature) + '.png')
    plt.clf()

# Create a Partial Dependence Plot for a specific feature and find the maximum value
pdp_data, _ = partial_dependence(model_rf, X, features=[features_info['features'][0]])
feature_values = pdp_data[0][0]
partial_dependence_values = pdp_data[1][0]
max_index = np.argmax(partial_dependence_values)
max_value = partial_dependence_values[max_index]
max_feature_value = feature_values[max_index]

# Plot the PDP data
plt.figure(figsize=(8, 6))
plt.plot(feature_values, partial_dependence_values, marker='o', linestyle='-')
plt.plot(max_feature_value, max_value, marker='o', markersize=8, color='red', label='Max Value')
plt.xlabel(features_info['features'][0])
plt.ylabel('Partial Dependence')
plt.title(f'Partial Dependence Plot for {features_info["features"][0]}')
plt.legend()
plt.grid(True)
plt.show()

print(f"The maximum value in the PDP graph is: {max_value}")
print(f"It occurs at {features_info['features'][0]} = {max_feature_value}")
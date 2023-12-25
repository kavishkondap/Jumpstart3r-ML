import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import PartialDependenceDisplay, partial_dependence
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, f_regression

from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import joblib

# Set the style
# plt.style.use('fivethirtyeight')
import matplotlib as mpl  
mpl.rc('font',family='Times New Roman')

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

data['Media Type']-=1

X, x_val, y, y_val = train_test_split(data, labels, test_size=0.2)
var_columns = [c for c in data]

model_rf = RandomForestClassifier()
model_rf.fit(X, y)
# print (model_rf.feature_importances_)
print ('score', model_rf.score (x_val, y_val))

cross_val = cross_val_score (model_rf, x_val, y_val, cv=5, scoring='roc_auc')
print ('cross val', cross_val)
# joblib.dump (model_rf, './random_forest.joblib', compress=3)

df_var_imp = pd.DataFrame({'Variable': var_columns,
                           'Importance': model_rf.feature_importances_}) \
                .sort_values(by='Importance', ascending=False) \
                .reset_index(drop=True)

# Customize the bar plot
fig, ax = plt.subplots(figsize=(17, 15))
plt.subplots_adjust (left=0.18)
sorted = df_var_imp.sort_values('Importance')
hbars = ax.barh(list (sorted['Variable']), list (sorted['Importance']))
# ax.set_title('Feature Importance', fontname = 'Times New Roman')
ax.set_xlabel('Relative Importance', fontname = 'Times New Roman', fontsize = 30)
# ax.set_ylabel('Variable', fontname = 'Times New Roman', fontsize = 15)
vals = list (df_var_imp.sort_values('Importance')['Importance'])
print (vals)
print (type (hbars))
ax.bar_label (hbars, fmt='%.4f', fontname = 'Times New Roman', fontsize=22)
# Rotate x-axis labels and adjust figure size for wrapped text
plt.yticks(rotation='horizontal', wrap=True, fontname = 'Times New Roman', fontsize = 25)
plt.xscale ('log')
plt.tick_params(axis='x', which='minor')
plt.xticks (fontname = 'Times New Roman', fontsize = 30)


plt.show()

feature_options = list (data.keys())
print ('feats', len (feature_options))
for feature in feature_options:
    fig, ax = plt.subplots(figsize=(18, 12), sharey=True, constrained_layout=True)
    # fig.subplots_adjust(hspace=0.7, wspace=0.1)
    # ncols=2, 
    features_info = {
        "features": [str(feature)],
        "kind": "both",
        "centered": True,
    }
    common_params = {
        'n_jobs':-1,
        'random_state':42,
    }

    display = PartialDependenceDisplay.from_estimator(
        model_rf,
        X,
        **features_info,
        ax=ax,
        **common_params,
        pd_line_kw={"color": "black"},
    )
    _ = display.figure_.suptitle(f"ICE and PDP representations for {features_info['features'][0]}", fontsize=25)
    print ('saving figure')
    plt.legend (fontsize = 35)
    ax.xaxis.label.set_fontsize (25)
    ax.yaxis.label.set_fontsize (25)
    # plt.xlabel (ax.xaxis.get_label().get_text(), fontname = 'Times New Roman', fontsize = 15)
    # plt.ylabel (ax.yaxis.get_label().get_text(), fontname = 'Times New Roman', fontsize = 15)
    # plt.title (fontname = 'Times New Roman', fontsize = 25)
    plt.xticks (fontname = 'Times New Roman', fontsize = 15)
    plt.yticks (fontname = 'Times New Roman', fontsize = 15)
    plt.savefig ('PDP_'+str(feature)+'.png')
    plt.clf()


pdp_data, _ = partial_dependence(model_rf, X, features=[features_info['features'][0]])

# Extract the feature values and partial dependence values from the pdp_data
feature_values = pdp_data[0][0]
partial_dependence_values = pdp_data[1][0]

# Find the maximum value and its index in the partial dependence values
max_index = np.argmax(partial_dependence_values)
max_value = partial_dependence_values[max_index]
max_feature_value = feature_values[max_index]

# Plot the PDP data using Matplotlib
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
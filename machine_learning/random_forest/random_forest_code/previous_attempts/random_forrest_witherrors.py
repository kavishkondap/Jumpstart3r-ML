import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import PartialDependenceDisplay, partial_dependence
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.utils import resample
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV

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

X, x_val, y, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)
var_columns = [c for c in data]

rf_model = RandomForestClassifier()
rf_model.fit(X, y)
print (rf_model.feature_importances_)

print ('score', rf_model.score (x_val, y_val))
max_values = []
loc_of_max = []
errors = []

for feature in list (data.keys ()):
    print ('Running PDP for', feature)
    nox_values = np.linspace(np.min(X[feature]), np.max(X[feature]))

    pdp_values = []
    for n in nox_values:
        X_pdp = X.copy()
        X_pdp[feature] = n
        pdp_values.append(np.mean(rf_model.predict(X_pdp)))

    n_bootstrap = 100

    nox_values = np.linspace(np.min(X[feature]), np.max(X[feature]))

    expected_value_bootstrap_replications = []

    for i in range(n_bootstrap):
        X_boot, y_boot = resample(X, y)
        rf_model_boot = RandomForestClassifier(n_estimators=100).fit(X_boot, y_boot)
        
        bootstrap_model_predictions = []
        for n in nox_values:
            X_pdp = X_boot.copy()
            X_pdp[feature] = n
            bootstrap_model_predictions.append(np.mean(rf_model.predict(X_pdp)))
        expected_value_bootstrap_replications.append(bootstrap_model_predictions)
        if (i%25==0):
            print ("Done with", i, 'iterations out of', n_bootstrap)
        
    expected_value_bootstrap_replications = np.array(expected_value_bootstrap_replications)
    for ev in expected_value_bootstrap_replications:
        plt.plot(nox_values, ev, color='blue', alpha=.1)

    prediction_se = np.std(expected_value_bootstrap_replications, axis=0)
    max_values.append (np.max (pdp_values))
    loc_of_max.append (nox_values[np.argmax (pdp_values)])
    errors.append (prediction_se[np.argmax (pdp_values)])
    print ('Maximum (optimal value) for', feature, 'is', np.max (pdp_values), 'at', nox_values[np.argmax (pdp_values)])
    print ('The error on this max value is', prediction_se[np.argmax (pdp_values)])
    
    plt.plot(nox_values, pdp_values, label='Model predictions', color = 'black')
    plt.fill_between(nox_values, pdp_values - 3*prediction_se, pdp_values + 3*prediction_se, alpha=.5, label='Bootstrap CI')
    plt.legend()
    plt.ylabel('Likelihood of Campaign Success')
    plt.xlabel(feature)
    plt.title(f'Partial dependence plot for {feature}')
    plt.savefig ('PDP_witherror'+str (feature)+'.png')
    plt.clf()

df = pd.DataFrame ({'Features': list (data.keys ()),
                    'Maxes':max_values,
                    'Loc of Maxes':loc_of_max,
                    'Errors':errors}, columns=['Features', 'Maxes', 'Loc of Maxes', 'Errors'])
df.to_csv ('ERROR_PDP.csv')


# plt.plot(nox_values, pdp_values)
# plt.ylabel('Predicted house price')
# plt.xlabel('NOX')
# plt.title('Partial dependence plot for NOX vs Price for Random Forest')
# plt.show()
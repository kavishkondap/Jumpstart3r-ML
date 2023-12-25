import pandas as pd
import numpy as np

data2 = pd.read_csv('OtherData.csv')

currency_used = data2['currency']

net_currency = []
for curr in currency_used:
    if (curr not in net_currency):
        net_currency.append (curr)

print (net_currency)
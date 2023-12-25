import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

curr_data = pd.read_excel ("machineLearningData.xlsx")
other_data = pd.read_csv ('OtherData.csv')

for i in range (len (curr_data['ids'])):
    media = np.array ([curr_data['top_media'][i], curr_data['bottom_media'][i]])
    max_val = np.max (media)
    curr_data['top_media'][i] = max_val
    print (max_val)
exit()
geolocator = Nominatim(user_agent="MyApp")
locations = np.array (other_data['location'])
print (locations)
latitude = []
longitude = []
count = 0
for i in range (locations.size):
    print (locations [i])
    if (other_data['id'][i] in curr_data['ids']):
        locations [i] = locations[i][locations[i].index ('localized_name:')]
        count+=1
        # location = geolocator.geocode(locations [i])
        # latitude [i] = location.latitude
        # longitude [i] = location.longitude
print (count)
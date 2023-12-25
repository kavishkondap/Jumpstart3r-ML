import pandas as pd
from geopy.geocoders import Nominatim
import time

data = pd.read_excel ('machineLearningData9.xlsx')
locations = data ['locations']

latitudes = []
longitudes = []
# population = []
geolocator = Nominatim(user_agent="MyApp")

count = 0
for location in locations:
    try:
        coords = geolocator.geocode (location)
        latitudes.append (coords.latitude)
        longitudes.append (coords.longitude)
        print (location, latitudes[-1], longitudes[-1], count)
        count+=1
    except:
        latitudes.append ('')
        longitudes.append ('')
        print ("FAILED", location)
        count+=1

data ['latitudes'] = latitudes
data ['longitudes'] = longitudes

data.to_excel ('machineLearningData10.xlsx')
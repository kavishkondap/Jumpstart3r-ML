import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

data = pd.read_excel ('machineLearningData12.xlsx')
geolocator = Nominatim(user_agent="MyApp")


problem_indicies = []

# for i in range (len (data ['latitudes'])):
#     if not (data['latitudes'][i].isnumeric()):
#         problem_indicies.append (i)

# problem_indicies = data.isnull ().any()
problem_indicies = list(zip(*[x for x in list(map(list, np.where(np.isnan(np.array(data['latitudes'])))))]))

print (problem_indicies)
print (len (problem_indicies))
unusual = 0

for index in problem_indicies:
    # print (type (index))
    # print (index)
    index = index [0]
    location = data ['locations'][index]
    try:
        if (location == 'Cornwall and Isles of Scilly UK'):
            data ['latitudes'][index] = 50.266
            data ['longitudes'][index] = 5.0527
        elif (location == 'Springfield MO'):
            data ['latitudes'][index] = 37.1968298
            data ['longitudes'][index] = -93.2946576
        elif (location == "L'viv Ukraine"):
            data ['latitudes'][index] = 49.8397
            data ['longitudes'][index] = 24.0297   
        elif (location == 'UNUSUAL LOCATION PLACEMENT'):
            unusual+=1
            print (unusual)
        else:
            coords = geolocator.geocode (location)
            data ['latitudes'][index] = coords.latitude
            data ['longitudes'][index] = coords.longitude
        print (location, data ['latitudes'][index], data ['longitudes'][index], index)
    except:
        # latitudes.append ('')
        # longitudes.append ('')
        print ("FAILLED", location)
        # count+=1

print (problem_indicies)
print (len (problem_indicies))

data.to_excel ('machineLearningData13.xlsx')
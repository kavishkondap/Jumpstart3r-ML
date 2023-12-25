import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

data = pd.read_excel ('machineLearningData14.xlsx')

geolocator = Nominatim(user_agent="MyApp")

cities = [
    "Tokyo, Japan",
    "Delhi, India",
    "Shanghai, China",
    "São Paulo, Brazil",
    "Mexico City, Mexico",
    "Cairo, Egypt",
    "Mumbai, India",
    "Beijing, China",
    "Dhaka, Bangladesh",
    "Osaka, Japan",
    # "New York, United States",
    # "Karachi, Pakistan",
    # "Buenos Aires, Argentina",
    # "Chongqing, China",
    # "Istanbul, Turkey",
    # "Kolkata, India",
    # "Manila, Philippines",
    # "Lagos, Nigeria",
    # "Rio de Janeiro, Brazil",
    # "Tianjin, China",
    # "Kinshasa, DR Congo",
    # "Guangzhou, China",
    # "Los Angeles, United States",
    # "Moscow, Russia",
    # "Shenzhen, China",
    # "Lahore, Pakistan",
    # "Bangalore, India",
    # "Paris, France",
    # "Bogotá, Colombia",
    # "Jakarta, Indonesia",
    # "Chennai, India",
    # "Lima, Peru",
    # "Bangkok, Thailand",
    # "Seoul, South Korea",
    # "Nagoya, Japan",
    # "Hyderabad, India",
    # "London, United Kingdom",
    # "Tehran, Iran",
    # "Chicago, United States",
    # "Chengdu, China",
    # "Nanjing, China",
    # "Wuhan, China",
    # "Ho Chi Minh City, Vietnam",
    # "Luanda, Angola",
    # "Ahmedabad, India",
    # "Kuala Lumpur, Malaysia",
    # "Xi'an, China",
    # "Hong Kong, China",
    # "Dongguan, China",
    # "Hangzhou, China",
    # "Foshan, China",
    # "Shenyang, China",
    # "Riyadh, Saudi Arabia"
]

big_city_lat = []
big_city_long = []

for city in cities:
    coords = geolocator.geocode (city)
    big_city_lat.append (coords.latitude)
    big_city_long.append (coords.longitude)
    print (city, big_city_lat[-1], big_city_long[-1])

lat_storage = {}
long_storage = {}
for city in cities:
    lat_storage [city] = []
    long_storage [city] = []
print (lat_storage)
for i in range (len (data ['latitudes'])):
    for j in range (len (cities)):
            lat_diff = np.abs (data['latitudes'][i]-big_city_lat[j])
            # print (cities[i])
            lat_storage [cities[j]].append (lat_diff)

            long_diff = np.abs (data['longitudes'][i]-big_city_long[j])
            long_storage [cities[j]].append (long_diff)
    if (i%100==0):
        print (i)

# print (lat_storage)

for key in lat_storage.keys():
     data [key+'_lat'] = lat_storage[key]
     print (lat_storage[key])
for key in long_storage.keys ():
     data [key+'_long'] = long_storage [key]
     print (long_storage [key])

print ('pushing data')
data.to_excel ('machineLearningData16.xlsx')
from turtle import back
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import re

data = pd.read_excel ('KickstarterData.xlsx')
data2 = pd.read_csv('OtherData.csv')

#SUCCESS
success = np.array (data['success'])


# #TOP MEDIA
topVideo = np.array (data['topvideo'])
topImage = np.array (data ['topimage'])

topMedia = np.zeros (topVideo.size)
for i in range (topVideo.size):
    if (topVideo[i]==1):
        topMedia [i] = 2
    elif (topImage[i]==1):
        topMedia [i] = 1
print (topMedia)

# #BOTTOM MEDIA
bottomVideo = np.array (data['topvideo'])
bottomImage = np.array (data ['topimage'])

bottomMedia = np.zeros (bottomVideo.size)
for i in range (bottomVideo.size):
    if (bottomVideo[i]==1):
        bottomMedia [i] = 2
    elif (bottomImage[i]==1):
        bottomMedia [i] = 1
print (bottomMedia)
unusualThings = np.zeros (success.size)

# #LOCATION
geolocator = Nominatim(user_agent="MyApp")
locations = np.array (data ['location'])
latitude = np.zeros (locations.size)
longitude = np.zeros (locations.size)
# for i in range (locations.size):
#     if ',' in locations[i]:
#         locations [i] = locations[i][0:locations[i].index (',')]
#     location = geolocator.geocode(locations [i])
#     try:
#         latitude [i] = location.latitude
#         longitude [i] = location.longitude
#     except:
#         unusualThings [i] = 1



# #BLURBS
blurbs = data ['blurb'].astype ('str')

# #UPDATES
updates = np.array (data ['update'])

# #UNUSUAL WEBSITE DETECTOR
for i in range (updates.size):
    if (updates[i] =='UNUSUAL WEBSITE 2.0'):
        unusualThings [i] = 1

# #COMMENTS
comments = np.array (data ['comment'])
for i in range (comments.size):
    comments [i] = (re.sub (',', '', str(comments[i])))

# #BACKERS

backers = np.array (data2['backers_count'])
for i in range (backers.size):
    backers [i] = (re.sub (',', '', str(backers[i])))
#GOAL
count = 0
goalFails = 0
goalUnfor = np.array(data['goal'])
goalInts = ['']*goalUnfor.size#np.zeros (goalUnfor.size)
goalFloats = np.zeros (goalUnfor.size)
currencyUsed = np.zeros (goalUnfor.size)
for i in range (goalUnfor.size):
    hasDec = False
    iterationHelper = goalUnfor[i]
    for j in range (len (str(iterationHelper))):
        if ((str(goalUnfor[i]))[j:j+1].isdigit ()):
                currNum =str(goalInts[i])
                currNum += ((str(goalUnfor[i]))[j:j+1])
                goalInts [i] = currNum
        # elif j==0 and (str(goalUnfor[i]))[j:j+1].isdigit():
        #     goalInts.append (((str(goalUnfor[i]))[j:j+1]))
        elif ((((str(goalUnfor[i]))[j:j+1]) == '.') and not hasDec):
            hasDec = True
            currNum =str(goalInts[i])
            currNum += ((str(goalUnfor[i]))[j:j+1])
            goalInts [i] = currNum
    # print (goalInts[i])
    try:
        goalFloats[i] = float(goalInts[i])
        if 'CA' in (str)(goalUnfor [i]):
            goalFloats [i] *= 0.77
            currencyUsed[i] = 1
        elif 'NOK' in (str)(goalUnfor [i]):
            goalFloats[i]*= 0.10
            currencyUsed[i] = 2
        elif 'DKK' in (str)(goalUnfor [i]):
            goalFloats[i] *= 0.14
            currencyUsed[i] = 3
        elif 'MX' in (str)(goalUnfor [i]):
            goalFloats [i] *=0.050
            currencyUsed[i] = 4
        elif '€' in (str)(goalUnfor [i]):
            goalFloats [i] *= 1.05
            currencyUsed[i] = 5
        elif '£' in (str)(goalUnfor [i]):
            goalFloats [i] *= 1.23
            currencyUsed[i] = 6
        elif '¥' in (str)(goalUnfor [i]):
            goalFloats [i] *= 0.0074
            currencyUsed[i] = 7
        elif 'HK' in (str)(goalUnfor [i]):
            goalFloats[i] *=0.13
            currencyUsed[i] = 8
        elif 'CHF' in (str)(goalUnfor [i]):
            goalFloats [i] *= 1.04
            currencyUsed[i] = 9
        elif 'PLN' in (str)(goalUnfor [i]):
            goalFloats [i] *=0.22
            currencyUsed[i] = 10
        elif 'AU' in (str)(goalUnfor [i]):
            goalFloats [i] *=0.69
            currencyUsed[i] = 11
        elif 'SEK' in (str)(goalUnfor [i]):
            goalFloats [i] *= 0.098
            currencyUsed[i] = 12
        elif 'NZ' in (str)(goalUnfor [i]):
            goalFloats [i] *= 0.63
            currencyUsed[i] = 13
        elif 'S' in (str)(goalUnfor [i]):
            goalFloats [i] *= 0.72
            currencyUsed[i] = 14
        elif '$' in (str)(goalUnfor [i]):
            random = 1
        else:
            count+=1
            unusualThings[i] = 1
            currencyUsed[i] = 15
            # print (i, goalUnfor [i])
    except:
        unusualThings[i] = 1
        goalFails+=1
# print (goalFails)


successNew = []
topMediaNew = []
bottomMediaNew = []
latitudeNew = []
longitudeNew = []
blurbsNew = []
commentsNew = []
updatesNew = []
backersNew = []
goalNew = []
currencyUsedNew = []

for i in range (unusualThings.size):
    if unusualThings[i]==0:
        # try:
        #     unusualThings = np.delete (unusualThings, i)
        #     success = np.delete (success, i)
        #     topMedia = np.delete (topMedia, i)
        #     bottomMedia = np.delete (bottomMedia, i)
        #     latitude = np.delete (latitude, i)
        #     longitude = np.delete (longitude, i)
        #     blurbs = np.delete (blurbs, i)
        #     comments = np.delete (comments, i)
        #     updates = np.delete (updates, i)
        #     backers = np.delete (backers, i)
        #     goalInts = np.delete (goalInts, i)
        #     currencyUsed = np.delete (currencyUsed, i)
        #     i -=1
        # except:
        #     print ("FAILED")
        #     print (i)
        successNew.append (success[i])
        topMediaNew.append (topMedia[i])
        bottomMediaNew.append (bottomMedia[i])
        latitudeNew.append (latitude[i])
        longitudeNew.append (longitude[i])
        blurbsNew.append (blurbs[i])
        commentsNew.append (comments[i])
        updatesNew.append (updates[i])
        backersNew.append (backers[i])
        goalNew.append (goalFloats[i])
        currencyUsedNew.append (currencyUsed[i])
newData = {'Success':successNew,
            'Top Media':topMediaNew,
            'Bottom Media':bottomMediaNew,
            'Latitude':latitudeNew,
            'Longitude':longitudeNew,
            'Comments':commentsNew,
            'Updates':updatesNew,
            'Backers':backersNew,
            'Goal':goalNew,
            'Currency Used':currencyUsedNew,
            'Blurbs':blurbsNew}

df = pd.DataFrame (newData, columns= ['Success',
                    'Top Media',
                    'Bottom Media',
                    'Latitude',
                    'Longitude',
                    'Comments',
                    'Updates',
                    'Backers',
                    'Goal',
                    'Currency Used',
                    'Blurbs'])

df.to_excel (r'C:/Users/kavis/Desktop/KAVISH/General Stuff/WebScraping/Machine Learning/dataProcessing.xlsx', index = False, header=True)

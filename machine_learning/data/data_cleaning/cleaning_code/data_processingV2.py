from turtle import back
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import re
from currency_conversions import curr_converter

data = pd.read_excel ('KickstarterData.xlsx')
data2 = pd.read_csv('OtherData.csv')

#SUCCESS
success = np.array (data['success'])
unusualThings = np.zeros (success.size)

#TITLE
title = np.array (data['title'])
for i, ttl in enumerate (title):
    try:
        t = len (ttl)
        if (ttl == "PRIVATE WEBSITE"):
            unusualThings[i] = 1
    except:
    # if (ttl == '' or ttl == None or not pd.isna (data.loc [i, 'title'])):
        unusualThings[i] = 1
    

# #TOP MEDIA
topVideo = np.array (data['topvideo'])
topImage = np.array (data ['topimage'])

topMedia = np.zeros (topVideo.size)
for i in range (topVideo.size):
    if (topVideo[i]):
        topMedia [i] = 2
    elif (topImage[i]):
        topMedia [i] = 1
# print (topMedia)

# #BOTTOM MEDIA
bottomVideo = np.array (data['topvideo'])
bottomImage = np.array (data ['topimage'])

bottomMedia = np.zeros (bottomVideo.size)
for i in range (bottomVideo.size):
    if (bottomVideo[i]):
        bottomMedia [i] = 2
    elif (bottomImage[i]):
        bottomMedia [i] = 1
# print (bottomMedia)

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
#     if (i % 100 ==0):
#         print (i)


# #BLURBS
blurbs = data ['blurb'].astype ('str')

# TYPE

category = data2['Category'].astype ('str')
for i in range (len (category)):
    category[i] = category[i][5:]

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
#GOAL (USD)

currencyUsed = data2['currency']
goalFloats = []
currencyNums = []
for i, goal in enumerate (data2['goal']):
    currencyNums.append (curr_converter [currencyUsed[i]])
    # print ("GOAL OBJECT: ", goal)
    goal = str (goal)
    # print (goal)
    # print (type (goal))
    goal_formatted = ''
    for j in range (len (goal)):
        if (goal[j].isnumeric () or goal [j] == '.'):
            goal_formatted+=goal[j]
    # print ("GOAL FORMATTED: ", goal_formatted)
    if (goal_formatted == ''):
        unusualThings[i] = 1
        goalFloats.append (goal_formatted) #appends a blank string
    else:
        # print ("GOAL: ", goal)
        goal_formatted = float (goal_formatted)
        # print ("FORMATTED: ", goal_formatted)
        goal_converted =  round (goal_formatted*curr_converter[currencyUsed[i]], 2)
        # print ("CONVERTED: ", goal_converted)
        goalFloats.append (goal_converted)

# AMOUNT RAISED (USD)
amount_raised = []

for i, amount in enumerate (data2['converted_pledged_amount']):
    amount_raised.append (amount)


# print (goalFails)

titleNew = []
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
currencyNumsNew = []
amount_raised_new = []

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
        titleNew.append (title[i])
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
        currencyNumsNew.append (currencyNums[i])
        amount_raised_new.append (amount_raised[i])
    
numCapitalsBlurbs = []
numNumbersBlurbs = []
numCapitalsTitle = []
numNumbersTitle = []

for blurb in blurbsNew:
    numCapitals = 0
    numNum = 0
    for i in range (len (blurb)):
        if (blurb[i].isupper()):
            numCapitals+=1
        if (blurb[i].isnumeric ()):
            numNum+=1
    numCapitalsBlurbs.append (numCapitals)
    numNumbersBlurbs.append (numNum)

for ttl in titleNew:
    numCapitals = 0
    numNum = 0
    try:
        for i in range (len (ttl)):
            if (ttl[i].isupper()):
                numCapitals+=1
            if (ttl[i].isnumeric ()):
                numNum+=1
        numCapitalsTitle.append (numCapitals)
        numNumbersTitle.append (numNum)
    except:
        print (ttl)
newData = { 'Title':titleNew,
            'Success':successNew,
            'Top Media':topMediaNew,
            'Bottom Media':bottomMediaNew,
            'Latitude':latitudeNew,
            'Longitude':longitudeNew,
            'Comments':commentsNew,
            'Updates':updatesNew,
            'Backers':backersNew,
            'Goal':goalNew,
            'Currency Used':currencyNumsNew,
            'Amount Raised': amount_raised_new,
            'Blurbs':blurbsNew,
            'Blurb Capitals':numCapitalsBlurbs,
            'Blurb Numbers':numNumbersBlurbs,
            'Title Capitals':numCapitalsTitle,
            'Title Numbers':numNumbersTitle}

df = pd.DataFrame (newData, columns= ['Title', 
                                    'Success',
                                    'Top Media',
                                    'Bottom Media',
                                    'Latitude',
                                    'Longitude',
                                    'Comments',
                                    'Updates',
                                    'Backers',
                                    'Goal',
                                    'Currency Used',
                                    'Amount Raised',
                                    'Blurbs',
                                    'Blurb Capitals',
                                    'Blurb Numbers',
                                    'Title Capitals',
                                    'Title Numbers'])

df.to_excel (r'C:/Users/kavis/Desktop/KAVISH/General Stuff/WebScraping/Machine Learning/dataProcessing3.xlsx', index = False, header=True)



# {id:2289476,project_id:2289476,state:inactive,state_changed_at:1450855441,name:null,blurb:null,background_color:null,text_color:null,link_background_color:null,link_text_color:null,link_text:null,link_url:null,show_feature_image:false,background_image_opacity:0.8,should_show_feature_image_section:true,feature_image_attributes:{image_urls:{default:https://ksr-ugc.imgix.net/assets/012/338/191/2734ed747524c31b13e10d20fc1c0337_original.png?ixlib=rb-2.1.0&crop=faces&w=1552&h=873&fit=crop&v=1463755983&auto=format&frame=1&q=92&s=bcaca9d771db05415b41edddb8a7656c,baseball_card:https://ksr-ugc.imgix.net/assets/012/338/191/2734ed747524c31b13e10d20fc1c0337_original.png?ixlib=rb-2.1.0&crop=faces&w=560&h=315&fit=crop&v=1463755983&auto=format&frame=1&q=92&s=97399cefce5056331601e06bed1f61d9}}}
# {id:372420508,name:Jeremy Caldwell,slug:theultimatejeremy,is_registered:null,is_email_verified:null,chosen_currency:null,is_superbacker:null,avatar:{thumb:https://ksr-ugc.imgix.net/assets/006/290/491/431ae4d26db57bd97a1d25383e1b2371_original.jpg?ixlib=rb-2.1.0&w=40&h=40&fit=crop&v=1495522900&auto=format&frame=1&q=92&s=b8025f9f8f9615f2622d5a7b49ffe425,small:https://ksr-ugc.imgix.net/assets/006/290/491/431ae4d26db57bd97a1d25383e1b2371_original.jpg?ixlib=rb-2.1.0&w=80&h=80&fit=crop&v=1495522900&auto=format&frame=1&q=92&s=8dc7647717404919732e353e8ab576a4,medium:https://ksr-ugc.imgix.net/assets/006/290/491/431ae4d26db57bd97a1d25383e1b2371_original.jpg?ixlib=rb-2.1.0&w=160&h=160&fit=crop&v=1495522900&auto=format&frame=1&q=92&s=900cbcb5290ad924f2c7350344d62372},urls:{web:{user:https://www.kickstarter.com/profile/theultimatejeremy},api:{user:https://api.kickstarter.com/v1/users/372420508?signature=1608266765.13740df17604028225e1913bc6ee4e87e377ad89}}}
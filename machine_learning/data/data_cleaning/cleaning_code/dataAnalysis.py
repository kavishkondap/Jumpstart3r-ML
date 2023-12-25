import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel ("machineLearningData.xlsx")

# Percentage successful vs failed
num_successful = 0
num_failed = 0
for datum in data['successes']:
    if (datum==1):
        num_successful+=1
    elif (datum==0):
        num_failed+=1
    else:
        print ("FAILED", datum)
        exit ()

print ("Percent successful", (num_successful)/(num_successful+num_failed)*100)

num_top_video_successful = 0
num_top_video_failed = 0
num_top_video = 0
for i in range (len (data['successes'])):
    if (data['top_media'][i]==2):
        num_top_video+=1
        if (data['successes'][i]==1):
            num_top_video_successful+=1
        elif (data['successes'][i]==0):
            num_top_video_failed+=1
print (num_top_video_successful)
print (num_top_video_failed)
print (num_top_video)
print ("Percent successful", (num_top_video_successful)/(num_top_video_failed+num_top_video_successful)*100)
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
from lxml import etree
from successful_website_collector import get_successful_data

old_data = pd.read_excel ('machineLearningData.xlsx')
LINKS = old_data['urls'].to_numpy ()
# HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
HEADERS = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
NUM_LINKS = len (LINKS)
titles = []


def get_success (soup):
    success = soup.find('div', class_='Campaign-state-successful')
    if (success != None):
        return True
    else:
        return False

for i, link in enumerate (LINKS):
    page = requests.get(link, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    dom = etree.HTML(str(soup))
    success = old_data['successes'][i]
    # print (success)
    if success:
        # print ("in the if statement")
        website_data = get_successful_data (soup, dom)
        # print ("found successful data")
        if (website_data[1]==1):
            titles.append (website_data[0])
            print ("Found error:", website_data[0])
        
data = pd.read_excel ("machineLearningData.xlsx")
count = 0
for i in range (len (data['titles'])):
    if data['titles'][i] in titles:
        data['top_media'][i] = 2
        count+=1
        print (count)
# print (count)
data.to_excel ('machineLearningDataV2.xlsx')
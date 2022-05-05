# Writing to an excel 
# sheet using Python
import xlwt
from xlwt import Workbook
import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import tweepy
import time
from time import sleep
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\main table plus socials plus genre plus chains plus devices.xls')

ss2 = r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\RankToEarn.net\RankToEarn\src\assets\img'


id_ = []
name = []
disc_url = []
twitter_url = []
route = []
home_page = []
img_path = []
P2E_Url = []
telegram = []
github = []
youtube = []
twitch = []
facebook = []
instagram = []
reddit = []
medium = []
gitbook = []
bitcointalk = []
steam = []
genres = []
blockchains = []
devices = []

###Load main table
id_ = df2['id'].tolist()
name = df2['name'].tolist()
disc_url = df2['disc_url'].tolist()
twitter_url = df2['twitter_url'].tolist()
route = df2['route'].tolist()
home_page = df2['home_page'].tolist()
img_path = df2['img_path'].tolist()
P2E_Url = df2['P2E Url'].tolist()
telegram = df2['telegram'].tolist()
github = df2['github'].tolist()
youtube = df2['youtube'].tolist()
twitch = df2['twitch'].tolist()
facebook = df2['facebook'].tolist()
instagram = df2['instagram'].tolist()
reddit = df2['reddit'].tolist()
medium = df2['medium'].tolist()
gitbook = df2['gitbook'].tolist()
bitcointalk = df2['bitcointalk'].tolist()
steam = df2['steam'].tolist()
genres = df2['genres'].tolist()
blockchains = df2['blockchains'].tolist()
devices = df2['devices'].tolist()

# Acess site
# Acess specs.json
# See if there is a galery
# if false, write on specs: "proj_status":"none"
# if true:
#   loop through tags:
#       try:
#           download img
#           img_counter += 1
#       except:
#   write on specs: "galery_sie":img_counter

i = 0
for page in P2E_Url:
    name_fix = name[i].replace(":","")
    specs_path = ss2 + '\\' + name_fix + '\\' + 'specs.json'
    with open(specs_path, 'r') as f:
        specs = json.load(f)
    print('Project:',specs['project'])
    
    r = requests.get(page)
    soup = BeautifulSoup(r.text, 'html.parser')
    mylinks = soup.find_all("div", {"class": "item"})
    if(str(mylinks) == '[]'):
        print('no galery here hermano')
        specs['img_count'] = 0
    else:
        img_count = 0
        img_path = ss2 + '\\' + name_fix + '\\'
        for div in mylinks:
            words = str(div).split(' ')
            for word in words:
                if('href=' in word):
                    
                    link = word.replace('''href="''',"")
                    link = link.replace('''">\n<img''',"")
                    
                    img_data = requests.get(link).content
                    with open(img_path + str(img_count) + '.png', 'wb') as handler:
                        handler.write(img_data)
                    print(img_count,link)
                    img_count += 1
        specs['img_count'] = img_count
        assemble_mid = json.dumps(specs)
        with open(specs_path, 'w') as outfile:
            outfile.write(assemble_mid)

    print('testing specs[img_count] =',specs['img_count'])
                    

    #if(i == 3): break
    sleep(5)
    i += 1



















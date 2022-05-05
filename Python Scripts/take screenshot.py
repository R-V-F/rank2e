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

#page height = 1080

#if h = 2474 -> 0 1080 2160 2474

df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\main table plus socials plus genre plus chains plus devices.xls')

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


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

ss2 = r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\RankToEarn.net\RankToEarn\src\assets\img'
i = 0
for page in home_page:
    if(i > 763):
        name_fix = name[i].replace(":", "")
    
        specs_path = ss2 + '\\' + name_fix + '\\' + 'specs.json'

        assemble = {}
        assemble['id'] = id_[i]
        assemble['project'] = name[i]
        
        
        if(page != 'none'):
            
            try:
                driver.get(page)
                sleep(0.5)
                el = driver.find_element_by_tag_name('body')
                el.screenshot( ss2 + '\\' + name_fix + '\\' + 'web_page' + '.png')
                assemble['web_status'] = 'try'
            except:
                print('shiiiiiieeet...', i)
                assemble['web_status'] = 'except'


        else:
            assemble['web_status'] = 'none'
        
        assemble_mid = json.dumps(assemble)
        with open(specs_path, 'w') as outfile:
            outfile.write(assemble_mid)
    


        
        print(i)
    i += 1



driver.quit()
print("end...")

import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
import re
import xlwt
from xlwt import Workbook
import shutil # save img locally
import os
import os.path
from os import path
import json

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
id_list = df2['id'].tolist()
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


##json_data is sorted by id
with open('json_data.json', 'r') as f:
  data = json.load(f)


i = 0
main_table_index = 0
for table in data['tables']:
    for id_ in id_list: #main table -> find axie in main table
        if(table['id'] == id_):
            break
        main_table_index += 1
    
    table['img_path'] = img_path[main_table_index]
    table['route'] = route[main_table_index]
    
    table['socials'] = {}
    if(twitter_url[main_table_index] != 'DEL'):
        table['socials']['twitter'] = twitter_url[main_table_index]
    else:
        table['socials']['twitter'] = 'none'
    if(disc_url[main_table_index] != 'DEL'):
        table['socials']['discord'] = disc_url[main_table_index]
    else:
        table['socials']['discord'] = 'none'
    table['socials']['home_page'] = home_page[main_table_index]
    table['socials']['telegram'] = telegram[main_table_index]
    table['socials']['github'] = github[main_table_index]
    table['socials']['youtube'] = youtube[main_table_index]
    table['socials']['twitch'] = twitch[main_table_index]
    table['socials']['facebook'] = facebook[main_table_index]
    table['socials']['instagram'] = instagram[main_table_index]
    table['socials']['reddit'] = reddit[main_table_index]
    table['socials']['medium'] = medium[main_table_index]
    table['socials']['gitbook'] = gitbook[main_table_index]
    table['socials']['bitcointalk'] = bitcointalk[main_table_index]
    table['socials']['steam'] = steam[main_table_index]

    
    table['genres'] = genres[main_table_index]
    table['blockchains'] = blockchains[main_table_index]
    table['devices'] = devices[main_table_index]
 

    
##    print(json.dumps(table, indent=4)) 
##    if(i == 10):
##        f.close()
##        exit()
    i += 1
    main_table_index = 0


new_json = json.dumps(data)
with open('json_data_appended.json','w') as outfile:
    outfile.write(new_json)


f.close()

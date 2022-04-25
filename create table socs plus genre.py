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
import json

df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\main table plus socials complete lesgo.xls')

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


  
# Workbook is created
wb = Workbook()
  
## add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

## id	name	disc_url	twitter_url	route	home_page	img_path	P2E Url

## list_of_socials = ['twitter','discord', 'website', 'telegram', 'github', 'youtube', 'twitch', 'facebook', 'instagram', 'reddit', 'medium', 'gitbook', 'bitcointalk', 'steam']
##write headers

sheet1.write(0, 0, 'id')
sheet1.write(0, 1, 'name')
sheet1.write(0, 2, 'disc_url')
sheet1.write(0, 3, 'twitter_url')
sheet1.write(0, 4, 'route')
sheet1.write(0, 5, 'home_page')
sheet1.write(0, 6, 'img_path')
sheet1.write(0, 7, 'P2E Url')
sheet1.write(0, 8, 'telegram')
sheet1.write(0, 9, 'github')
sheet1.write(0, 10, 'youtube')
sheet1.write(0, 11, 'twitch')
sheet1.write(0, 12, 'facebook')
sheet1.write(0, 13, 'instagram')
sheet1.write(0, 14, 'reddit')
sheet1.write(0, 15, 'medium')
sheet1.write(0, 16, 'gitbook')
sheet1.write(0, 17, 'bitcointalk')
sheet1.write(0, 18, 'steam')
sheet1.write(0, 19, 'genres')




i=0
for id__ in id_:
    sheet1.write(i+1, 0, id__)
    sheet1.write(i+1, 1, name[i])
    sheet1.write(i+1, 2, disc_url[i])
    sheet1.write(i+1, 3, twitter_url[i])
    sheet1.write(i+1, 4, route[i])
    sheet1.write(i+1, 5, home_page[i])
    sheet1.write(i+1, 6, img_path[i])
    sheet1.write(i+1, 7, P2E_Url[i])
    sheet1.write(i+1, 8, telegram[i])
    sheet1.write(i+1, 9, github[i])
    sheet1.write(i+1, 10, youtube[i])
    sheet1.write(i+1, 11, twitch[i])
    sheet1.write(i+1, 12, facebook[i])
    sheet1.write(i+1, 13, instagram[i])
    sheet1.write(i+1, 14, reddit[i])
    sheet1.write(i+1, 15, medium[i])
    sheet1.write(i+1, 16, gitbook[i])
    sheet1.write(i+1, 17, bitcointalk[i])
    sheet1.write(i+1, 18, steam[i])


    i+=1

i = 0
timer = 0
##list_of_socials = ['telegram', 'github', 'youtube', 'twitch', 'facebook', 'instagram', 'reddit', 'medium', 'gitbook', 'bitcointalk', 'steam']
for url in P2E_Url:
    #if(i % 4 == 0 and i != 0): break
    time.sleep(3)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    mylinks = soup.find_all("div", {"class": "dapp_categories"})
    
    if(not str(mylinks) == '[]'):    
        
        genres = str(mylinks).split(' ')

        list_of_genres = []
        genre_flag = 0
        block_counter = 0
        for block in genres:
            if('href=' in block):
                genre_instance = genres[block_counter+1]
                #genre_instance = genre_instance.replace(" ", "")
                list_of_genres.append(genre_instance)
                genre_flag = 1
            block_counter += 1
        
        print('\ni =',i,'STRING:\n')
        if(genre_flag == 0):
            sheet1.write(i+1, 19, 'none')
            print('writing on',name[i],': none')
        else:
            string = ''
            ind = 0
            while(ind < len(list_of_genres)):
                string += list_of_genres[ind]
                if(not ind == len(list_of_genres) - 1): string += ','
                ind += 1
            sheet1.write(i+1, 19, string)
            print('writing on',name[i],':',string)
            
        
    ##    socials = str(mylinks).split('<a class="btn btn-outline-success" ')
        
    else:
        sheet1.write(i+1, 19, 'none')
        print('writing on',name[i],': none. PAGE NOT FOUND BABIII i =', i)
    i += 1






wb.save('main table plus socials complete lesgo plus genre.xls')
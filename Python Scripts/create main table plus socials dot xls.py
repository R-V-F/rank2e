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

df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\main table.xls')

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

id_ = df2['id'].tolist()
name = df2['name'].tolist()
disc_url = df2['disc_url'].tolist()
twitter_url = df2['twitter_url'].tolist()
route = df2['route'].tolist()
home_page = df2['home_page'].tolist()
img_path = df2['img_path'].tolist()
P2E_Url = df2['P2E Url'].tolist()

  
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

    i+=1

i = 0
timer = 0
list_of_socials = ['telegram', 'github', 'youtube', 'twitch', 'facebook', 'instagram', 'reddit', 'medium', 'gitbook', 'bitcointalk', 'steam']
for url in P2E_Url:

    time.sleep(3)    

    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    mylinks = soup.find_all("div", {"class": "social"})
    socials = str(mylinks).split('<a class="btn btn-outline-success" ')

    flag = 0
    if(str(mylinks) == '[]'):
        x1 = 8
        while(x1 < 19):
            print('\n************************* EMPTY *********************************')
            print(url)
            print('\n************************* EMPTY *********************************')
            sheet1.write(i+1, x1, 'none')
            x1 += 1
        flag = 1

    if(flag == 0):
    
        words = []    

        #[0 tel,0 git,0 yt,0 tw,0 face,0 insta,0 reddit,0 medium,0 gitbook,0 bittalk,0 steam]
        social_tracker = [0,0,0,0,0,0,0,0,0,0,0]
            
        for social in socials:
            if('href=' in social and 'socialimg' in social):
                words = social.split(' ') #divide into list of words
                i2 = 0
                x = 0
                print('social =',social)
                for word in words:
                    print('word =', word)
                    if(word == 'socialimg'):
                        print('we entered bois')
                        social_platform_name = words[i2+1]
                        social_platform_name = social_platform_name.replace('"','')
                        if(social_platform_name in list_of_socials):
                            if(social_platform_name == 'telegram'):
                                x = 8
                                social_tracker[0] = 1
                            if(social_platform_name == 'github'):
                                x = 9
                                social_tracker[1] = 1
                            if(social_platform_name == 'youtube'):
                                x = 10
                                social_tracker[2] = 1
                            if(social_platform_name == 'twitch'):
                                x = 11
                                social_tracker[3] = 1
                            if(social_platform_name == 'facebook'):
                                x = 12
                                social_tracker[4] = 1
                            if(social_platform_name == 'instagram'):
                                x = 13
                                social_tracker[5] = 1
                            if(social_platform_name == 'reddit'):
                                x = 14
                                social_tracker[6] = 1
                            if(social_platform_name == 'medium'):
                                x = 15
                                social_tracker[7] = 1
                            if(social_platform_name == 'gitbook'):
                                x = 16
                                social_tracker[8] = 1
                            if(social_platform_name == 'bitcointalk'):
                                x = 17
                                social_tracker[9] = 1
                            if(social_platform_name == 'steam'):
                                x = 18
                                social_tracker[10] = 1
                            if(x == 0): break

                            
                            
                            social_platform_link = words[0] #href="link"
                            social_platform_link = social_platform_link.replace('href="', '')
                            social_platform_link = social_platform_link.replace('"', '')

                            sheet1.write(i+1, x, social_platform_link)
                            
                            
                            
                            print('\nUrl:', url)
                            print('writing* line:', i+1, 'column:',x, 'link:', social_platform_link)
                            print('social_platform_name =', social_platform_name)
                            print('social_platform_name =', social_platform_link, '\n')
                            break
                        
                        
                    i2 += 1
        print('final state of social_tracker:\n', social_tracker)
        column = 8
        for have in social_tracker:
            if(not have):
                sheet1.write(i+1, column, 'none')
                print('filling* line:',i+1, 'column:',column, 'link: none')
            column += 1

           
    i += 1









  
  
wb.save('main table plus socials complete lesgo.xls')

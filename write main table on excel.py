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



conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HN763SI;'
                      'Database=disc_db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
query = 'SELECT * FROM new_pair_ID_table'





#converting pair_id_table to pandas df -> lists of url and id
df = pd.read_sql(query, conn)

cursor.close()
conn.close()


df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\img links.xls')


##From new_pair_id_table
pair_ID = []
proj_Name = []
proj_URL = []
proj_twitter_url = []

##From excel
p2e_url = []
##To routes
routes = []

##Home Page
home_page = []

###Load
pair_ID = df['pair_ID'].tolist()
proj_Name = df['proj_Name'].tolist()
proj_URL = df['proj_URL'].tolist()
proj_twitter_url = df['proj_twitter_url'].tolist()

p2e_url = df2['P2E Url'].tolist()

##Extracting routes
for url in p2e_url:
    url_split = url.split('/')
    route = url_split[len(url_split)-1].lower()
    routes.append(route)

##Extracting Home_Page + Inputing my own UTM
i = 0
page = ''
page_utm = '?utm_source=PlayToEarnRanks.net&utm_medium=organic&utm_campaign=gamepage' ##CHANGE THIS WHEN DECIDING THE BRAND NAME
timer_index = 0
soc_split = []
for url in p2e_url:
    timer_index += 1
    index = 0
    if(timer_index % 20 == 0):
        for link in home_page:
            print(link)
        time.sleep(30)

    list_of_socials = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    mylinks = soup.find_all("a", {"class": "btn btn-outline-success"})
    space_split = (str(mylinks)).split(" ")
    

    ##Fill list_of_socials
    for string in space_split:
        check = 'btn-outline-success"'
        if(check in string):
            social = space_split[index+1].replace('href="', "")
            social = social.replace('"',"")
            if(social[len(social)-1] == '/') : social = social[:-1] #pop last
            list_of_socials.append(social)
            #print(social)
        index += 1
        #print(string)

    ##Extract home_page link + input my own UTM
    page_flag = 0
    for soc in list_of_socials:
        if('source=PlayToEarn.net' in soc):
            page_flag = 1
            print('Flag = 1 *************************')
            print('soc =',soc, '\n')
            
            soc_split = soc.split("?")
            print('soc_split =',soc_split, '\n')

            page = soc_split[0] + page_utm
            print('page =',page, '\n')
            
            home_page.append(page)
            print('*********************************')
            
    if(page_flag == 0):
        page = 'none'
        print('Flag = 0 *************************')
        print('page =',page, '\n')
        home_page.append(page)
        print('*********************************')
    time.sleep(1)


    i += 1
    



# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

#write headers
sheet1.write(0, 0, 'id')
sheet1.write(0, 1, 'name')
sheet1.write(0, 2, 'disc_url')
sheet1.write(0, 3, 'twitter_url')
sheet1.write(0, 4, 'route')
sheet1.write(0, 5, 'home_page')


i=0
for project in proj_Name:
    sheet1.write(i+1, 0, pair_ID[i])
    sheet1.write(i+1, 1, project)
    sheet1.write(i+1, 2, proj_URL[i])
    sheet1.write(i+1, 3, proj_twitter_url[i])
    sheet1.write(i+1, 4, routes[i])
    sheet1.write(i+1, 5, home_page[i])
    
    i+=1



wb.save('main table.xls')






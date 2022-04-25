import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
import re
import xlwt
from xlwt import Workbook

##
##conn = pyodbc.connect('Driver={SQL Server};'
##                      'Server=DESKTOP-HN763SI;'
##                      'Database=disc_db;'
##                      'Trusted_Connection=yes;')
##cursor = conn.cursor()
##query = 'SELECT * FROM new_pair_ID_table'
##
##
##proj_list = []
##
###converting pair_id_table to pandas df -> lists of url and id
##df = pd.read_sql(query, conn)
##
##proj_list = df['proj_Name'].tolist()
##p2edotnet_list = []
##img_link_list = []
##
##cursor.close()
##conn.close()
##
##i=0
##for project in proj_list:
##    
##
##    if(' ' in project):
##        name = project.replace(' ','-')
##        print(i,'Project:',project)
##        print('https://playtoearn.net/blockchaingame/'+name)
##        url = 'https://playtoearn.net/blockchaingame/'+name
##        p2edotnet_list.append(url)
##       
##    else:
##        print('Project',project)
##        print('https://playtoearn.net/blockchaingame/'+project)
##        url = 'https://playtoearn.net/blockchaingame/'+project
##        p2edotnet_list.append(url)
##    i+=1
##    
##i=0
##for link in p2edotnet_list:
##    r = requests.get(link)
##    soup = BeautifulSoup(r.text, 'html.parser')
##    mydivs = soup.find_all("div", {"class": "dapp_profilepic"})
##    result = str(mydivs)
##    result = result.split('src="')
##    img_link = result[len(result)-1].replace(""""/>\n</div>]""","")
##    print(i, link,':')
##    print(img_link)
##    img_link_list.append(img_link)
##    i+=1
##    if(i % 14 == 0): time.sleep(23)
##    
##
##
##
##
##
##
### Workbook is created
##wb = Workbook()
##  
### add_sheet is used to create sheet.
##sheet1 = wb.add_sheet('Sheet 1')
##
###write headers
##sheet1.write(0, 0, 'Project')
##sheet1.write(0, 1, 'P2E Url')
##sheet1.write(0, 2, 'P2E Image Url')
##
##i=0
##for project in proj_list:
##    sheet1.write(i+1, 0, project)
##    sheet1.write(i+1, 1, p2edotnet_list[i])
##    sheet1.write(i+1, 2, img_link_list[i])
##    i+=1
##
##
##
##wb.save('img links.xls')

df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\img links.xls')

project_list = []
url_list = []
img_url_list = []


project_list = df2['Project'].tolist()
url_list = df2['P2E Url'].tolist()
img_url_list = df2['P2E Image Url'].tolist()

i=0
timer = 1
for link in img_url_list:

    if('[]' in link): 
        
        google_search = project_list[i] + " playtoearn.net site:playtoearn.net"
        print('i:', i, '\ngogle_search:',google_search)
        search_url = "https://www.google.com/search?q=" + google_search
        r = requests.get(search_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup.prettify())
        raw = str(soup.h3.parent)
        split = raw.split("q=")
        split2 = split[1].split("&")
        page_link = split2[0]
        print('page link before:', url_list[i])
        url_list[i] = page_link
        print('page link now:', url_list[i])

        
        r2 = requests.get(page_link)
        soup2 = BeautifulSoup(r2.text, 'html.parser')
        mydivs = soup2.find_all("div", {"class": "dapp_profilepic"})
        result = str(mydivs)
        result = result.split('src="')
        img_link = result[len(result)-1].replace(""""/>\n</div>]""","")
        print('image link before:', img_url_list[i])
        img_url_list[i] = img_link
        print('image link now:', img_url_list[i])
        
        if(timer % 10 == 0): time.sleep(30)
        timer += 1
        
    if(link == '%%'):
        page_link = url_list[i]
        r2 = requests.get(page_link)
        soup2 = BeautifulSoup(r2.text, 'html.parser')
        mydivs = soup2.find_all("div", {"class": "dapp_profilepic"})
        result = str(mydivs)
        result = result.split('src="')
        img_link = result[len(result)-1].replace(""""/>\n</div>]""","")
        print('image link before:', img_url_list[i])
        img_url_list[i] = img_link
        print('image link now:', img_url_list[i])

        if(timer % 10 == 0): time.sleep(45)
        timer +=1
        
        


    i+=1
    


# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

#write headers
sheet1.write(0, 0, 'Project')
sheet1.write(0, 1, 'P2E Url')
sheet1.write(0, 2, 'P2E Image Url')

i=0
for project in project_list:
    sheet1.write(i+1, 0, project)
    sheet1.write(i+1, 1, url_list[i])
    sheet1.write(i+1, 2, img_url_list[i])
    i+=1



wb.save('img links2.xls')














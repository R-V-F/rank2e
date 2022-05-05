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


df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\img links.xls')

project_list = []
url_list = []
img_url_list = []
json_url_list = []


project_list = df2['Project'].tolist()
url_list = df2['P2E Url'].tolist()
img_url_list = df2['P2E Image Url'].tolist()

list_of_failed_downloads = []

i=0

for project in project_list:
    if(':' in project):
        project_name = project.replace(':','')
    else:
        project_name = project
    if(True):
        directory = project_name
        parent_dir = r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\RankToEarn.net\RankToEarn\src\assets\img'
        ##create folder
        path_ = os.path.join(parent_dir, directory)
        flag = False
        flag = path.exists(path_)
        
##        if(flag == False):
##            os.mkdir(path_)
        print('\n\n#######################################')
        if(flag == False): print("Directory '% s' created" % path_)
        else: print('Directory already exisits:', path_)


        ##download file
        #DEFAULT URL: #https://playtoearn.net/img/dapp/uninterest-unicorns/profile_picture/100_uninterest-unicorns.png
        if(img_url_list[i] == 'default'):
            url = 'https://playtoearn.net/img/dapp/uninterest-unicorns/profile_picture/100_uninterest-unicorns.png'
            file_name = 'default.png'
            file_path = r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\RankToEarn.net\RankToEarn\src\assets\img'
            file_name_path = os.path.join(file_path, project_name, file_name)

            json_split = file_name_path.split('src')
            json_path = json_split[len(json_split)-1]
            json_url_list.append(json_path)
            
            print('url: DEFAULT')
            print('file_name:', file_name)
            print('file_path:', file_path)
            print('file_name_path:', file_name_path)
            print('json_path:', json_path)
            
##            if(flag == False):
##                res = requests.get(url, stream = True)
##                if res.status_code == 200:
##                    with open(file_name_path,'wb') as f:
##                        shutil.copyfileobj(res.raw, f)
##                    print('Image sucessfully Downloaded: ',file_name)
##                else:
##                    print('Image Couldn\'t be retrieved')
##                    list_of_failed_downloads.append(project_name)
##                print('#######################################')
                 
        
        else:
            split_url = img_url_list[i].split('/')
            file_name = split_url[len(split_url)-1]
            file_path = r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\RankToEarn.net\RankToEarn\src\assets\img'
            file_name_path = os.path.join(file_path, project_name, file_name)
            url = img_url_list[i]
            
            json_split = file_name_path.split('src')
            json_path = json_split[len(json_split)-1]
            json_url_list.append(json_path)
            
            print('url:',url)
            print('file_name:', file_name)
            print('file_path:', file_path)
            print('file_name_path:', file_name_path)
            print('json_path:', json_path)
            
##            if(flag == False):
##                res = requests.get(url, stream = True)
##                if res.status_code == 200:
##                    with open(file_name_path,'wb') as f:
##                        shutil.copyfileobj(res.raw, f)
##                    print('Image sucessfully Downloaded: ',file_name)
##                else:
##                    print('Image Couldn\'t be retrieved')
##                    list_of_failed_downloads.append(project_name)
##                print('#######################################')
            
        #time.sleep(4)
            
    i+=1
    

for fail in list_of_failed_downloads:
    print(fail)


# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

#write headers
sheet1.write(0, 0, 'Project')
sheet1.write(0, 1, 'P2E Url')
sheet1.write(0, 2, 'P2E Image Url')
sheet1.write(0, 3, 'JSON Url')

i=0
for project in project_list:
    sheet1.write(i+1, 0, project)
    sheet1.write(i+1, 1, url_list[i])
    sheet1.write(i+1, 2, img_url_list[i])
    sheet1.write(i+1, 3, json_url_list[i])
    
    i+=1



wb.save('img links with paths lesgo.xls')





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



id_list = []

#converting pair_id_table to pandas df -> lists of url and id
df = pd.read_sql(query, conn)

cursor.close()
conn.close()


df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\img links with paths lesgo.xls')

project_list = []
url_list = []
img_url_list = []
json_url_list = []

id_list = df['pair_ID'].tolist()
project_list = df2['Project'].tolist()
json_url_list = df2['JSON Url'].tolist()



# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

#write headers
sheet1.write(0, 0, 'id')
sheet1.write(0, 1, 'Project')
sheet1.write(0, 2, 'Img Path')


i=0
for project in project_list:
    sheet1.write(i+1, 0, id_list[i])
    sheet1.write(i+1, 1, project)

    sheet1.write(i+1, 2, json_url_list[i])
    
    i+=1



wb.save('id_project_img-path.xls')













    

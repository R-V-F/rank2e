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
  
# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

#write headers
sheet1.write(0, 0, 'Name')
sheet1.write(0, 1, 'Url')
sheet1.write(0, 2, 'Twitter')


with open('json_projects.json', 'r') as f:
  data = json.load(f)

##each roll is an object in data['projects']
i = 0
while(i<len(data['projects'])):
    sheet1.write(i+1, 0, data['projects'][i]['name'])
    sheet1.write(i+1, 1, data['projects'][i]['discord'])
    sheet1.write(i+1, 2, data['projects'][i]['twitter'])
    
    i += 1
  


  
  
wb.save('xlwt addfile.xls')

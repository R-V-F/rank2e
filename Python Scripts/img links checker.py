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


df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\img links.xls')

project_list = []
url_list = []
img_url_list = []


project_list = df2['Project'].tolist()
url_list = df2['P2E Url'].tolist()
img_url_list = df2['P2E Image Url'].tolist()

i=0
for img in img_url_list:
    if(img != 'default'):
        if(not('100' in img)):
            print('\nURL(i):', img, '(',i,')')

    i += 1

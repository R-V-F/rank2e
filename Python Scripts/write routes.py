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

df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\id route file.xlsx')

proj_id = []
proj_route = []

proj_id = df2['id'].tolist()
proj_route = df2['route'].tolist()



i=0
for route in proj_route:
    path = """{path: '"""+route+"""', component: PageComponent, data: {id:'"""+str(proj_id[i])+"""'}},"""
    print(path)
    i += 1
    

#{path: '(route)', component: PageComponent, data : {id:'(id)'}}










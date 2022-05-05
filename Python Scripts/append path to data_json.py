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

with open('json_data.json', 'r') as f:
  data = json.load(f)


df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\id_project_img-path.xls')


excel_id_list = []
excel_path_list = []



excel_id_list = df2['id'].tolist()
excel_path_list = df2['Img Path'].tolist()

i = 0

for id_ in excel_id_list:
    j = 0
    while(j < len(data['tables'])):
        if(data['tables'][j]['id'] == id_):
           data['tables'][j]['img_path'] = excel_path_list[i]

        j += 1

    i += 1

print(json.dumps(data, indent=4))

new_json = json.dumps(data)
with open('json_data_w_img.json','w') as outfile:
    outfile.write(new_json)

























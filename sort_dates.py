import json
import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import time

# reads a 'json_data.json' file
with open('json_data_appended.json', 'r') as f:
  data = json.load(f)

##sorting dates

h = 0
k = 1
j = 0
aux_date = 0
aux_mem = 0
while (h < len(data['tables'])):
    while (k < len(data['tables'][h]['dates'])):
        
        while (j < len(data['tables'][h]['dates'])-k):
            if(data['tables'][h]['dates'][j] > data['tables'][h]['dates'][j+1]):
                aux_date = data['tables'][h]['dates'][j]
                aux_mem = data['tables'][h]['members'][j]

                data['tables'][h]['dates'][j] = data['tables'][h]['dates'][j+1]
                data['tables'][h]['members'][j] = data['tables'][h]['members'][j+1]

                data['tables'][h]['dates'][j+1] = aux_date
                data['tables'][h]['members'][j+1] = aux_mem
                
            j += 1


        j = 0
        
        k += 1
        
    k = 1
    h += 1



    

##sorting dates TWITTER

h = 0
k = 1
j = 0
aux_date = 0
aux_mem = 0
while (h < len(data['tables'])):
    while (k < len(data['tables'][h]['twt_dates'])):
        
        while (j < len(data['tables'][h]['twt_dates'])-k):
            if(data['tables'][h]['twt_dates'][j] > data['tables'][h]['twt_dates'][j+1]):
                aux_date = data['tables'][h]['twt_dates'][j]
                aux_mem = data['tables'][h]['followers'][j]

                data['tables'][h]['twt_dates'][j] = data['tables'][h]['twt_dates'][j+1]
                data['tables'][h]['followers'][j] = data['tables'][h]['followers'][j+1]

                data['tables'][h]['twt_dates'][j+1] = aux_date
                data['tables'][h]['followers'][j+1] = aux_mem
                
            j += 1


        j = 0
        
        k += 1
        
    k = 1
    h += 1





sorted_json = json.dumps(data)
with open('json_data_appended_and_sorted.json','w') as outfile:
    outfile.write(sorted_json)




outfile.close()
f.close()














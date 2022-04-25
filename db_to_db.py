import json
import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import time



now = datetime.now()
date_time = now.strftime("%m/%d/%Y")
##yesterday = datetime.today() - timedelta(days=1)
##date_time = yesterday.strftime("%m/%d/%Y")
####^^^^^^^^^^^ in case u fuq up

# Directory
directory = date_time.replace("/","")

json_data_path = './backup/'+directory+'/json_data.json'

with open(json_data_path, 'r') as f:
  data = json.load(f)



###POP THE 0 ENTRIES
###IF 1 ENTRY == 0 -> POP
tables_index = 0
members_index = 0
flag = 0

pop_list = []

###CREATE LIST WITH INDEXES TO POP (POP_LIST)
while(tables_index<len(data['tables'])):
    while (members_index < len(data['tables'][tables_index]['members'])):
        if(data['tables'][tables_index]['members'][members_index] == 0):
            flag = 1 ##raise flag if there's a 0 element
        members_index += 1

    if(flag == 1):
        pop_list.append(tables_index)
    


    members_index = 0
    tables_index += 1
    flag = 0


###POP'EM!
pop_list_index = 0
iterator = 0

while (pop_list_index < len(pop_list)):
    
    data['tables'].pop(pop_list[pop_list_index])
    ##updating the indexes (need to subtract one after poping bc list is shorter)
    while (iterator<len(pop_list)):
        pop_list[iterator] = pop_list[iterator] -1
        iterator += 1

    iterator = 0
    pop_list_index += 1


###TEST V
tables_index = 0
members_index = 0
flag = 0

pop_list2 = []
while(tables_index<len(data['tables'])):
    while (members_index < len(data['tables'][tables_index]['members'])):
        if(data['tables'][tables_index]['members'][members_index] == 0):
            flag = 1 ##raise flag if there's a 0 element
        members_index += 1

    if(flag == 1):
        pop_list2.append(tables_index)
    


    members_index = 0
    tables_index += 1
    flag = 0

if(pop_list2):
    print(pop_list2)
else:
    print('YAHOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO LESGOOO')

######## END OF TEST


########SORT'EM

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












print(data['tables'][0]['dates'])
print(data['tables'][0]['members'])
print(data['tables'][1]['dates'])
print(data['tables'][1]['members'])
print(data['tables'][2]['dates'])
print(data['tables'][2]['members'])



json_path = './backup/'+directory+'/json_data_modified.json'




new_json = json.dumps(data)
with open(json_path,'w') as outfile:
    outfile.write(new_json)




outfile.close()
f.close()


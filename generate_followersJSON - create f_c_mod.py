import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import tweepy
import time
import json
 
# Opening JSON file
f2 = open('followers_count.json')
followers = json.load(f2)

#####################

with open('json_data.json', 'r') as f:
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


print(pop_list,len(pop_list))


###POP'EM!
pop_list_index = 0
iterator = 0

while (pop_list_index < len(pop_list)):

    print('POPPING raw_id:',data['tables'][pop_list[pop_list_index]+pop_list_index]['id']-1)
    print('POPPING raw_name:',data['tables'][pop_list[pop_list_index]+pop_list_index]['name'])
    print('POPPING raw_VALUE:',followers['followers_count'][pop_list[pop_list_index]])
    
    followers['followers_count'].pop(pop_list[pop_list_index])
    ##updating the indexes (need to subtract one after poping bc list is shorter)
    while (iterator<len(pop_list)):
        pop_list[iterator] = pop_list[iterator] -1
        iterator += 1

    iterator = 0
    pop_list_index += 1

print(pop_list, len(pop_list))

print(len(data['tables']))




new_json = json.dumps(followers)
with open('followers_count_modified.json','w') as outfile:
    outfile.write(new_json)



print(len(followers['followers_count']))

 

# Closing file
f.close()
f2.close()






import json
import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

with open('json_data.json', 'r') as f:
  data = json.load(f)


##print(json.dumps(data, indent=4))
print(len(data['tables'])) #338


list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
slist = []
slist.append(list1)
slist.append(list2)

print(slist[0][0])

super_list = []

##make super_list -> list of list of members
i=0
while i<len(data['tables']):
    super_list.append(data['tables'][i]['members'])
    i+=1

print(super_list)

###check for 0 entries so u dont divide by 0
###I'm not going by week, rather, last-first
growth_list = []
growth=0
i=0
while i<len(data['tables']):
    i2 = len(super_list[i])
    if(super_list[i][0] != 0):
        growth = (super_list[i][i2-1])/(super_list[i][0])
    else:
        growth = -2
    growth_list.append(growth)
    i+=1

print(len(growth_list))
print(growth_list)


###percentage list
no_percentage = -2
growth_list_percentage = []
i=0
while i<len(growth_list):
    if(growth_list[i] != -2):
        percentage = (growth_list[i]-1)*100
        growth_list_percentage.append(percentage)
    else:
        growth_list_percentage.append(no_percentage)

    
    i+=1

print(len(growth_list_percentage))
print(growth_list_percentage)

##pricking the index of the bigger number
i=0
j=0
while j<len(growth_list):
    if(growth_list[j]>growth_list[i]):
        i=j
    j+=1

print(growth_list[i])
print(data['tables'][i]['members'])

i=0
j=0
while j<len(growth_list):
    if(growth_list[j]>growth_list[i] and growth_list[j]!= growth_list[13] and growth_list[j] != growth_list[134] and growth_list[j] != growth_list[45]):
        i=j
    j+=1
print(i)
print(growth_list[i])
print(data['tables'][i]['name'])
print(data['tables'][i]['members'])




###TODO
##how to deal with [88,88,...] repeated entries
##what if i'm trying to search out of range
##(ex: weekly growth but only 5 days data)
##what if weird data start appearing?
##([1140,1160,1165,9999,9999,9999])
####run algo to catch these anomalies












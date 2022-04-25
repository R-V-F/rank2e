import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
import json


##IF:
### NOT FIRST LETTER IS CAPS
### AND NEXT LETTER IS NOT CAPS
### ADD SPACE BEFORE THE CAP LETTER
def add_space(testw):

    j=0
    str1 = ''
    i = 0
    flag = 0
    while (i<len(testw)):
        if (i != (len(testw)-1) and i != 0):
            if(testw[i].isupper() and not testw[i+1].isupper() and testw[i-1] != ' '):
                while(j<i):
                    
                    str1 += testw[j]
                    j += 1
                str1 += ' '
                while (i<len(testw)):
                    str1 += testw[i]
                    i += 1
                flag = 1
        
        i += 1

    if(flag == 1): return (str1)
    else: return testw


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HN763SI;'
                      'Database=disc_db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
query = 'SELECT * FROM new_pair_ID_table'

name_list = []

#converting table to pandas df
df = pd.read_sql(query, conn)



name_list = df['proj_Name'].tolist()

i=0

list_one = []


for word in name_list:
    #print(name_list[i],'(id:', i+1, ')' ,': ', add_space(word))
    list_one.append(add_space(word))
    i += 1

list_two = []

i=0

for word in list_one:
    #print(list_one[i],'(id:', i+1, ')' ,': ', add_space(word))
    list_two.append(add_space(word))
    i += 1

#print(list_two)


##
##update pair_ID_table
##set proj_twitter_url = 'https://twitter.com/stepheronfts'
##where pair_id = 3380;

i=0
for word in list_two:

    _sql = """\
    IF OBJECT_ID('new_pair_ID_table') IS NOT NULL
        BEGIN
            update new_pair_ID_table
            set proj_Name = '"""+word+"""'
            where pair_ID = """+str(i+1)+""";
        END;
  
    """

    print(_sql)
    i += 1
    cursor.execute(_sql)


    
conn.commit()
cursor.close()
conn.close()























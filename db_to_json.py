import json
import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import time
import os


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HN763SI;'
                      'Database=disc_db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
query = 'SELECT * FROM new_pair_ID_table'


url_list = []
id_list = []

#converting pair_id_table to pandas df -> lists of url and id
df = pd.read_sql(query, conn)

url_list = df['proj_URL'].tolist()
id_list = df['pair_ID'].tolist()
name_list = df['proj_Name'].tolist()




##TODO
#create 'db' and db.json
#for table_id_pair.length()
#   read id, name, from table_id_pair then:
#       table_id: read dates; read members;

##THE PROBLEM:
# Given that I have: Id, Name, dates[] and members[]
# How do I make the db?


#db
assemble = {}


#cria 'tables' e define como lista
assemble['tables'] = []
#query das tables
query2 = 'SELECT * FROM table_'

##ind = 0
##while(ind<len(id_list)):
##    assemble['tables'].append({})
##    ind += 1

initial = 429
for id_ in id_list:
    correct_id = ((id_+428) % 805) + 1
    query_new2 = 'SELECT * FROM table_'+str(correct_id)+'F'
    print(query_new2)
    df3 = pd.read_sql(query_new2, conn)
    followers_list = df3['Followers'].tolist()
    date_followers_list = df3['Date'].tolist()

    
    
    query_new = 'SELECT * FROM table_' + str(correct_id)
    print(query_new)
    df2 = pd.read_sql(query_new, conn)
    members_list = df2['Members'].tolist()
    date_list = df2['Date'].tolist()


    
    assemble['tables'].append({})
    assemble['tables'][correct_id-1]['id'] = correct_id
    #print('i(id):',i,'\nname:',name_list[i-1],'\nmembers',members_list,'\ndate_list',date_list,'\nfollowers:',followers_list,'\ndates f list:',date_followers_list)
    assemble['tables'][correct_id-1]['name'] = name_list[initial % 805]
    assemble['tables'][correct_id-1]['members'] = members_list
    assemble['tables'][correct_id-1]['dates'] = date_list
    assemble['tables'][correct_id-1]['followers'] = followers_list
    assemble['tables'][correct_id-1]['twt_dates'] = date_followers_list

    initial += 1
    
    #print(i)
    #i+=1




print(json.dumps(assemble, indent=4))
assemble_mid = json.dumps(assemble)

assemble_go = json.loads(assemble_mid)
print(assemble_go["tables"][1]["members"])

print(len(id_list))

now = datetime.now()
date_time = now.strftime("%m/%d/%Y")
##yesterday = datetime.today() - timedelta(days=1)
##date_time = yesterday.strftime("%m/%d/%Y")
####^^^^^^^^^^^ in case u fuq up
 
# Directory
directory = date_time.replace("/","")
  
# Parent Directory path
parent_dir = r"C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\backup"
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory

os.mkdir(path)
print("Directory '% s' created" % path)

json_path = './backup/'+directory+'/json_data.json'


with open(json_path, 'w') as outfile:
    outfile.write(assemble_mid)

cursor.close()
conn.close()










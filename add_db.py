# DOCKER:
# A PLACE WHERE I PUT THE NAME/URL AND CHECK TO SEE IF THERE IS DUPLICATED URLS
# CHECK AGAINST PAIR_ID_TABLE
# IF THE SAME URL IS FOUND, SKIP
# THE RESULT MUST BE A LIST OF NEW URLS ONLY
import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime

new_url = 'https://discord.com/invite/me3X4zU8Uy'


## Connect to db, import pair_id_table
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HN763SI;'
                      'Database=disc_db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
query = 'SELECT * FROM new_pair_ID_table'

url_list = []
id_list = []

#converting table to pandas df
df = pd.read_sql(query, conn)

url_list = df['proj_URL'].tolist()
id_list = df['pair_ID'].tolist()

df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\xlwt addfile.xls')

url_list_to_add = df2['Url'].tolist()
name_list_to_add = df2['Name'].tolist()
twitter_list_to_add = df2['Twitter'].tolist()


pair_list_to_add = list(zip(name_list_to_add, url_list_to_add))

verified_url_list = []
verified_name_list = []
verified_twitter_list = []

print(pair_list_to_add)


## This checks for double entries and repeated entries
## 
index = 0
flag_count = 0
flag_list = []
for url in url_list_to_add:
    flag = 0 # 0 is no copy found
    ##check for double entries ON THE add_file.xlsx
    for verified_url in verified_url_list:
        url2 = url
        url2 = url2.split('/')
        verified_url2 = verified_url 
        verified_url2 = verified_url2.split('/')
        if(url2[len(url2)-1] == verified_url2[len(verified_url2)-1]):
            flag = 1
            print('double entry detected:' + name_list_to_add[index])

    ##check for URLs that are already IN THE DATA BASE
    for db_url in url_list:
        url2 = url
        url2 = url2.split('/')
        db_url2 = db_url
        db_url2 = db_url2.split('/')
        if(url2[len(url2)-1] == db_url2[len(db_url2)-1]):
            flag = 1
            flag_count += 1
            print('flaggy flaggy senpai:' + name_list_to_add[index])
            flag_list.append(name_list_to_add[index])
    if(flag == 0):
        verified_url_list.append(url)
        verified_name_list.append(name_list_to_add[index])
        verified_twitter_list.append(twitter_list_to_add[index])
        
        ###ADD VERIFIED TWITTER LIST
    index += 1


#print(list(zip(verified_name_list, verified_url_list)))

## Now I have to add to the PAIR_ID_TABLE

# generate list of IDs according to the last one found in the db

print(len(url_list))

# the first id will be len+1

first_id = len(url_list) + 1
verified_id_list = []
for a in verified_url_list:
    verified_id_list.append(first_id)
    first_id += 1

###FIX NAMING
fixed_name_list = []

for name in verified_name_list:
    fix = name.replace("-"," ")
    fix_cap = fix.title()

    fixed_name_list.append(fix_cap)
    
for word in fixed_name_list:
    print(word)
###

index = 0

if not verified_id_list:
    print('WEEEEEEEEEEEEEEE ARE THE CHAMPIONS, MY FREEN')

for id_ in verified_id_list:        
    _sql = """\
    BEGIN
        INSERT INTO new_pair_ID_table VALUES
        ("""+str(id_)+""", '"""+fixed_name_list[index]+"""', '"""+verified_url_list[index]+"""', '"""+verified_twitter_list[index]+"""')
    END;
    """
    ###CHANGE TABLE BEING AFFECTED
    cursor.execute(_sql)
    print('inserting into pair_id:'+str(id_)+', '+verified_name_list[index]+', '+verified_url_list[index])
    print(_sql)
    index += 1

print('FLAG COUNT:',flag_count)
my_dict = {i:flag_list.count(i) for i in flag_list}
print(my_dict)

for key in my_dict:
    if(my_dict[key]>1): print(key,'->',my_dict[key])



conn.commit()
cursor.close()
conn.close()

#now, I must set a goal of minimum urls added per day.
#or 1 pomo per day.


#figure how to plot the data















    

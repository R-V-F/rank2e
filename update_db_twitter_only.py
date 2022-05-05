import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import tweepy
import time
import json

def get_followers(twitter_acc_url):
    req_part1 = 'https://api.twitter.com/2/users/by/username/'
    req_part2 = '?user.fields=public_metrics,created_at'



    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMQHagEAAAAAzTQtZAD%2FaN1T3NVhFlnRbADBZzI%3DG9KEwjpqdBE5nYKAu5tYBYmb5Zgi1mTKmB3fPpNLMKDfMBTgKU',
    }

    if(twitter_acc_url != 'DEL'):
        ##getting the user
        split = twitter_acc_url.split('/')
        ##split[len(split)-1] --> last split
        req_assembled = req_part1 + split[len(split)-1] + req_part2
        
        response = requests.get(req_assembled, headers=headers)
        json = response.json()
        if "data" in json:
            return(json['data']['public_metrics']['followers_count'])
        else:
            print('Error with url:', twitter_acc_url)
            return -1

    else:
        return 0



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

url_list = df['proj_twitter_url'].tolist()
id_list = df['pair_ID'].tolist()

now = datetime.now()
##date_time = now.strftime("%m/%d/%Y")
yesterday = datetime.today() - timedelta(days=3)
date_time = yesterday.strftime("%m/%d/%Y")
#### ^^^^ in desperate times (i fuk up)

#adding sleep time so the requests dont get my ip banned
request_counter = 0



#if the table_id doesn't exist, it's created and the first value is inserted
#else, just insert the new data + date

##for id_ in id_list:
##    print(id_, '->',((id_+428) % 805) + 1 )
##
##print(id_list[0]) #377
##initial = 429
##
##for id_ in id_list:
####    print(id_, '->',((id_+428) % 805) + 1 )
##    print(initial, '->',(initial % 805))
##    initial += 1


initial = 429

for id_ in id_list:
    correct_id = ((id_+428) % 805) + 1
    count = get_followers(url_list[initial % 805])
    
    
    _sql = """\
    IF OBJECT_ID('table_"""+str(correct_id)+"""F') IS NOT NULL
        BEGIN
            INSERT INTO table_"""+str(correct_id)+"""F VALUES
            ("""+str(count)+""", '"""+date_time+"""' )
        END;
    ELSE
        BEGIN
            CREATE TABLE table_"""+str(correct_id)+"""F (
            Followers INT,
            Date VARCHAR(20)
            )
            INSERT INTO table_"""+str(correct_id)+"""F VALUES
            ("""+str(count)+""", '"""+date_time+"""' )

        END;

    """
    print(_sql)
    request_counter += 1
    initial += 1
    if(request_counter % 170 == 0): time.sleep(900)
    cursor.execute(_sql)
    

conn.commit()
    
cursor.close()
conn.close()



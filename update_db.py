import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import time

def get_memcount(url_link):
    r = requests.get(url_link)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Hacky solution. But it works
    raw_str = str(soup.meta.next_sibling.next_sibling.next_sibling.next_sibling)

    # Separates the part of the html into strings
    list_str = raw_str.split()

    # Searches for the string that starts with a digit, then see if there's a comma
    # This won't work for projects that have less than 1000 members
    # To fix it I think I have to better navigate the html

    for index in range(0, len(list_str)-1):
        if(list_str[index][0].isdigit()):
            for char in list_str[index]:
                if char == ',':
                    return(int(list_str[index].replace(',','')))

    return 0 #check manually the ones that return 0


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

now = datetime.now()
##date_time = now.strftime("%m/%d/%Y")
yesterday = datetime.today() - timedelta(days=2)
date_time = yesterday.strftime("%m/%d/%Y")
#### ^^^^ in desperate times (i fuk up)


#adding sleep time so the requests dont get my ip banned
request_counter = 0

initial = 429

#if the table_id doesn't exist, it's created and the first value is inserted
#else, just insert the new data + date

for id_ in id_list:
    correct_id = ((id_+428) % 805) + 1
    
    if(url_list[initial % 805] != 'DEL'):
        mem_count = get_memcount(url_list[initial % 805])
        _sql = """\
        IF OBJECT_ID('table_"""+str(correct_id)+"""') IS NOT NULL
            BEGIN
                INSERT INTO table_"""+str(correct_id)+""" VALUES
                ("""+str(mem_count)+""", '"""+date_time+"""' )
            END;
        ELSE
            BEGIN
                CREATE TABLE table_"""+str(correct_id)+""" (
                Members INT,
                Date VARCHAR(20)
                )
                INSERT INTO table_"""+str(correct_id)+""" VALUES
                ("""+str(mem_count)+""", '"""+date_time+"""' )

            END;

        """
    else:
        mem_count = -1
        _sql = """\
        IF OBJECT_ID('table_"""+str(correct_id)+"""') IS NOT NULL
            BEGIN
                INSERT INTO table_"""+str(correct_id)+""" VALUES
                ("""+str(mem_count)+""", '"""+date_time+"""' )
            END;
        ELSE
            BEGIN
                CREATE TABLE table_"""+str(correct_id)+""" (
                Members INT,
                Date VARCHAR(20)
                )
                INSERT INTO table_"""+str(correct_id)+""" VALUES
                ("""+str(mem_count)+""", '"""+date_time+"""' )

            END;

        """
        
    print(_sql)
    request_counter += 1
    initial += 1
    if(request_counter % 10 == 0): time.sleep(60)
    cursor.execute(_sql)



conn.commit()    
cursor.close()
conn.close()








print(url_list)


    


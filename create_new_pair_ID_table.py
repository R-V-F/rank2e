import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HN763SI;'
                      'Database=disc_db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\table_with_twitter_url.xlsx')

print(df2)

pair_id_list = df2['pair_ID'].tolist()
proj_name_list = df2['proj_Name'].tolist()

proj_url_list = df2['proj_URL'].tolist()
proj_twitter_url_list = df2['proj_twitter_url'].tolist()


print(proj_twitter_url_list)
print(pair_id_list)


for id_ in pair_id_list:        
    _sql = """\
    BEGIN
        INSERT INTO new_pair_ID_table VALUES
        ("""+str(id_)+""", '"""+proj_name_list[id_-1]+"""', '"""+proj_url_list[id_-1]+"""', '"""+proj_twitter_url_list[id_-1]+"""')
    END;
    """
    cursor.execute(_sql)
    
    print(_sql)
    



conn.commit()
cursor.close()
conn.close()


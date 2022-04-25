import json
import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time



conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HN763SI;'
                      'Database=disc_db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()




i=1
while (i<339):
    _sql = 'DROP TABLE table_'+str(i)+'F;'
    cursor.execute(_sql)
    print(_sql)
    i += 1



conn.commit()
cursor.close()
conn.close()




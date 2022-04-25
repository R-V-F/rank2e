import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime

## Connect to db, import pair_id_table
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HN763SI;'
                      'Database=disc_db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
query = 'SELECT * FROM pair_ID_table'

pair_id = 3

_sql = """\
declare @last_mem_count as int
set @last_mem_count = (SELECT Members FROM dbo.table_"""+str(pair_id)+""" ORDER BY [DATE] DESC OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY)
print(@last_mem_count)
declare @a as int
set @a = @last_man_count
insert into dbo.test_table2 values("""+str(pair_id)+""", @a)
"""
cursor.execute(_sql)
#insert into test_table2 values("""+str(pair_id)+""", @last_men_count)
print(_sql)





conn.commit()
cursor.close()
conn.close()

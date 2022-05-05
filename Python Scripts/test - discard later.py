import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import tweepy
import time
import json
# importing os module
import os

assemble = {}
assemble['id'] = 2
assemble['project'] = 'bliblibli'

assemble_mid = json.dumps(assemble)
with open('teste.json', 'w') as outfile:
        outfile.write(assemble_mid)




    

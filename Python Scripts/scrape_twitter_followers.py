import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import tweepy
import time



df2 = pd.read_excel(r'C:\Users\Renan\Desktop\PyProjs\Dsic Tracker\table_with_twitter_url.xlsx')

proj_twitter_url_list = df2['proj_twitter_url'].tolist()



ordered_list_of_followers = []

req_part1 = 'https://api.twitter.com/2/users/by/username/'
req_part2 = '?user.fields=public_metrics,created_at'



headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMQHagEAAAAAzTQtZAD%2FaN1T3NVhFlnRbADBZzI%3DG9KEwjpqdBE5nYKAu5tYBYmb5Zgi1mTKmB3fPpNLMKDfMBTgKU',
}





i=0

while(i<len(proj_twitter_url_list)):

    print(proj_twitter_url_list[i])
    if(proj_twitter_url_list[i] != 'DEL'):
        ##getting the user
        split = proj_twitter_url_list[i].split('/')
        ##split[len(split)-1] --> last split
        req_assembled = req_part1 + split[len(split)-1] + req_part2
        
        response = requests.get(req_assembled, headers=headers)
        json = response.json()
        ordered_list_of_followers.append(json['data']['public_metrics']['followers_count'])

    else:
        ordered_list_of_followers.append(0)
        
    i += 1
    if(i % 150 == 0): time.sleep(900)

i=0

while(i<len(proj_twitter_url_list)):
    print(proj_twitter_url_list[i], ':',ordered_list_of_followers[i])

    
    i += 1

print(ordered_list_of_followers)

##response = requests.get('https://api.twitter.com/2/users/by/username/gametheorizing?user.fields=public_metrics,created_at', headers=headers)
##
##print(response.json())
##
##json = response.json()
##
##print(json['data']['public_metrics']['followers_count'])

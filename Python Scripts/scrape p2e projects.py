import pyodbc
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import tweepy
import time
import json


##url_link = 'https://playtoearn.net/blockchaingames?sort=socialscore_24h&direction=desc&page='
##page_index = 1
##
##
##
##
################## FILL PAGE URL LIST -- ADD sleep time -> 10s
##page_url_list = []
##
##page_index = 1
##while(page_index<=22):
##    page_url = url_link + str(page_index)
##    page_url_list.append(page_url)
##    page_index += 1
##################
##
##project_url_list = []
##
##i=0
##
##for url in page_url_list:
##    i += 1
##    if(i % 10 == 0): time.sleep(15)
##    
##    r = requests.get(url)
##    soup = BeautifulSoup(r.text, 'html.parser')
##    mydivs = soup.find_all("a", {"class": "dapp_detaillink"})
##    row = (str(mydivs)).split('\n')
##    check = '"dapp_detaillink socialscoregraph"'
##    
##
##    for each in row:
##        if(check in each):
##            dirty = each.split('href="')
##            string = dirty[1].replace("""">""","")
##            project_url_list.append(string)
##
##            
## 
##for project in project_url_list:
##    print(project+',')
##
##
####now I have list of pages and list of URLS YUHU
##
##f = open('URL of Projects P2E.txt','r')
##giant_list = f.read()
##
##links = giant_list.split(',')
##corrected_links = []
##i=0
##for link in links:
##    if(i == 0): corrected_links.append(link)
##    else: corrected_links.append(link[1:])
##    i += 1
##
##timer_index = 0
##
##assemble = {}
##assemble['projects'] = []
##
##i=0
##
##
##for url in corrected_links:
##    timer_index += 1
##    if(timer_index % 20 == 0):
##        print(json.dumps(assemble, indent=4))
##        time.sleep(30)
##
##    list_of_socials = []
##    ##url = 'https://playtoearn.net/blockchaingame/light-trail-rush'
##    r = requests.get(url)
##    soup = BeautifulSoup(r.text, 'html.parser')
##
##    mylinks = soup.find_all("a", {"class": "btn btn-outline-success"})
##
##    space_split = (str(mylinks)).split(" ")
##    index = 0
##
##    ##Fill list_of_socials
##    for string in space_split:
##        check = 'btn-outline-success"'
##        if(check in string):
##            social = space_split[index+1].replace('href="', "")
##            social = social.replace('"',"")
##            if(social[len(social)-1] == '/') : social = social[:-1]
##            list_of_socials.append(social)
##            #print(social)
##        index += 1
##        #print(string)
##
##    
##
##    ##Fill object
##    assemble['projects'].append({})
##
##
##    name_split = url.split('/')
##    name = name_split[len(name_split)-1]
##    assemble['projects'][i]['name'] = name
##    twitter_flag = 0
##    discord_flag = 0
##    for soc in list_of_socials:
##        if('twitter' in soc):
##            assemble['projects'][i]['twitter'] = soc
##            twitter_flag = 1
##        if('discord' in soc):
##            assemble['projects'][i]['discord'] = soc
##            discord_flag = 1
##    if(twitter_flag == 0): assemble['projects'][i]['twitter'] = 'DEL'
##    if(discord_flag == 0): assemble['projects'][i]['discord'] = 'DEL'
##
##    i += 1
##
##
##
##
##print(json.dumps(assemble, indent=4))
##
##
##assemble_mid = json.dumps(assemble)
##
##assemble_go = json.loads(assemble_mid)
##
##
##with open('json_projects.json', 'w') as outfile:
##    outfile.write(assemble_mid)

url = 'https://playtoearn.net/blockchaingame/pepo-paradise'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

mylinks = soup.find_all("div", {"class": "social"})
socials = str(mylinks).split('<a class="btn btn-outline-success" ')
words = []
list_of_socials = ['telegram', 'github', 'youtube', 'twitch', 'facebook', 'instagram', 'reddit', 'medium', 'gitbook', 'bitcointalk', 'steam']




for social in socials:
    if('href=' in social and 'socialimg' in social):
        words = social.split(' ') #divide into list of words
        i2 = 0
        for word in words:
            if(word == 'socialimg'):
                social_platform_name = words[i+1]
                social_platform_name = social_platform_name.replace('"','')
                if(social_platform_name in list_of_socials):
                    social_platform_link = words[0] #href="link"
                    social_platform_link = social_platform_link.replace('href="', '')
                    social_platform_link = social_platform_link.replace('"', '')
                    
                    print('weee:')
                    print(social_platform_name)
                    print(social_platform_link)
                    break
                
                
            i2 += 1













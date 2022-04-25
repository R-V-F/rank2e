from bs4 import BeautifulSoup
import requests


##TODO
# How to store the pair name:url
## append in a dict?
# How to deal with expired invites
# How to deal with <1000 members

def get_memcount(url_link):
    r = requests.get(url_link)
    soup = BeautifulSoup(r.text, 'html.parser')

    #print(soup)

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

    return 0


    


url = 'https://discord.com/invite/QxruGXKV'

print(get_memcount(url))

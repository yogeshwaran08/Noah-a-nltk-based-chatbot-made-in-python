
import requests
from bs4 import BeautifulSoup
import random
import urllib


def get_trending_news(*args, **kwargs):
    url = 'https://www.bbc.com/news'
    conectivity = False
    trenNews = []
    try:
        conectivity = True
        urllib.request.urlopen('http://google.com')
    except:
        return random.choice(["You are not connected to internet", "Alas! You are not connected", "No internet!"])
    
    if (conectivity == True):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')
        unwanted = ['BBC World News TV', 'BBC World Service Radio', 'News daily newsletter', 'Mobile app', 'Get in touch']
        for x in list(dict.fromkeys(headlines)):
            if x.text.strip() not in unwanted:
                trenNews.append(x.text.strip())

        return random.choice(trenNews)
    
    else:
        return random.choice(["Sorry, Something went wrong", "Something Looks wrong here","You are not Connected"])
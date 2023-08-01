import urllib.request
import random

def connect(*args, **kwargs):
    try:
        urllib.request.urlopen('http://google.com')
        return random.choice(["You are connected to Internet", "Awsome, You are connected", "Everything Looks Good. You Are connected"])
    except:
        return random.choice(["You are not connected to internet", "Alas! You are not connected", "No internet!"])

from random import choice
from .nlp_engine import ResponseCreator

def noanswer(*args):   
    return choice(["Sorry i didn't catch that", "I can't understand"])

def nameSkill(*args):
    return choice(["My name is Noah", "I am Noah", "People call Noah"])

def whatCanYouDo(*args):
    return choice(["I can Make You laugh, search on google and So on", "I can Do anything For boss"])

def apologySkill(*args):
    return choice(["Sorry to hear that", "Apology, I will fix myself"])

def thankingSkill(*args):
    return choice(["Nice to hear that", "Thank You"])

def whatAreYouDoing(*args):
    return choice(["Reading Some books To gain more knowledge", 
    "Just searching a way to help You", 
    "Reading Some Jokes. Would You like to hear? Ask me 'Tell me a joke'"])

def loveYou(*args):
    return choice(["Love You Too!!!!", "How sweet!!Love u Too"])

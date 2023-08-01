import random

from scipy import rand

def howAreYou(*args):
    return random.choice(['I am Fine, Thanks for asking', "I am Good. Hope You Too","I am Well, That's Very nice to hear"])


def greet(*args):
    return random.choice(['Hello', "Hi", "hello Buddy"])

def bye(*args):
    return random.choice(['Good bye', "See You", "Tataa"])
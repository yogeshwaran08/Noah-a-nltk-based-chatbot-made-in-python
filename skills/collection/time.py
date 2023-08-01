from datetime import datetime

def timer(*args, **kwargs):
    return "It's " + str(datetime.now().strftime("%H:%M")) + " now"

def date(*args, **kwargs):
    return "Today's Date is "+ str(datetime.now().strftime("%d-%B-%Y"))
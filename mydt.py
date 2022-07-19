import datetime
now = datetime.datetime.now()
d = now.strftime("%H:%M:%p %d %B %Y")

def get_time():
    d = now.strftime("%H:%M:%p %d %B %Y")
    return(str(d))

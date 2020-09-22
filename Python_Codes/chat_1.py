from datetime import datetime as dt

hello_intent = ["hello", "hi", "hey", "hello there", "hi there"]
date_intent = ["tell me date","today's date","date","what's the date"]
time_intent = ["tell me time","current time","time","what's the time"]

while True:
    msg = input("Enter your message : ")

    if msg in hello_intent:
        print("Hello User")
    elif msg in date_intent:
        d = dt.now().date()
        print(d.strftime("%d/%m/%y,%a"))
    elif msg in time_intent:
        t = dt.now().time()
        print(t.strftime("%H:%M:%S,%p"))
    elif msg == "bye":
        print("Bye User")
        break
    else:
        print("I don't understand")


'''
>>> import os
>>> os.chdir(r"C:\Users\asus\Music")
>>> songs = os.listdir()
>>> import random
>>> s = random.choice(songs)
>>> os.startfile(s)
'''

















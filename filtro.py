import csv
import pandas as pd
from datetime import datetime
import numpy as np
from operator import attrgetter


global now
now = datetime.now()

def tiempoTranscurrido(date):
    global now
    return (now-date).days

DB = pd.read_csv("covid19_tweets.csv")
print("Las columnas son",DB.keys())
#print(pd.read_csv("covid19_tweets.csv")
print(DB)
print("FECHAS",type(DB.date[1]))
print("Hola :D")
# aaaa-mm-dd hh:mm:ss
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
DB.date = pd.to_datetime(DB.date)
DB = DB.sort_values( by='date', ascending=True )
DB = DB.reset_index()
print(DB["date"])
for  i in range(5):
    print(DB["date"][i],tiempoTranscurrido(DB["date"][i]))


#print("la fecha más antigua es:", DB.sort_values('date',ascending=False))



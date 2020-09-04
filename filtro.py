import csv
import pandas as pd
from datetime import datetime
import numpy as np
from operator import attrgetter

DB = pd.read_csv("covid19_tweets.csv")
print("Las columnas son",DB.keys())
#print(pd.read_csv("covid19_tweets.csv")
print("FECHAS",type(DB.date[1]))
print("Hola :D")
# aaaa-mm-dd hh:mm:ss
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
DB.date = pd.to_datetime(DB.date, format="%Y-%m-%d %H:%M:%S")
DB=DB.sort_values( 'date', ascending=True )
print(DB.date.to_string(),len(DB.date.to_string()))

#print("la fecha más antigua es:", DB.sort_values('date',ascending=False))

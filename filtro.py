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
DB=DB.sort_values( 'date', ascending=False )

#print("la fecha más antigua es:", DB.sort_values(('date'),ascending=(False))

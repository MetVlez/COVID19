#Crea una función que se encargue de mostrar cuántos tweets por ciudad han sido publicados

import csv
import pandas as pd
from datetime import datetime
from operator import attrgetter

DB = pd.read_csv("covid19_tweets.csv")
print("Las columnas son",DB.keys())
#print(DB["user_location"])
#Lizeth
locations = list(set(DB["user_location"].values))
#print(len(locations),len(DB["user_location"]))
locations = 


for user_location in DB["user_location"].values:
  print(user_location)
#Tener un listado tuyo de paises y siglas

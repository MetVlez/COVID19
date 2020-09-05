#Crea una función que se encargue de mostrar cuántos tweets por ciudad han sido publicados

import csv
import pandas as pd
from datetime import datetime
from operator import attrgetter

DB = pd.read_csv("covid19_tweets.csv")
print("Las columnas son",DB.keys())
#print(DB["user_location"])
#Lizeth
#print(len(locations),len(DB["user_location"]))
locations = {}
for location in list(set(DB["user_location"].values)):
  locations[location] = 0
for user_location in DB["user_location"].values:
  locations[user_location] += 1

for location in locations:
  print(location,".....Total de tweets en la ciudad:",locations[location])

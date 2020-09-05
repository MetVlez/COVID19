from datetime import date
import csv
import math
import pandas as pd
from datetime import datetime

DB = pd.read_csv("covid19_tweets.csv")
print("Las columnas son",DB.keys())
#print("usuario",type(DB.user_name[1]))


usuarios = {}
for usuario in list(set(DB["user_name"].values)):
  usuarios[usuario] = 0
for user_name in DB["user_name"].values:
  usuarios[user_name] += 1

for usuario in usuarios:
  #print(usuario,".....Total de tweets por usuario:",usuarios[usuario])
  print(max(usuarios,key=lambda i: usuarios[i]))
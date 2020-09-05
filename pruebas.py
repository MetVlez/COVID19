from datetime import date
import csv
import math
import pandas as pd
from datetime import datetime

DB = pd.read_csv("covid19_tweets.csv")
print("Las columnas son",DB.keys())
#print("usuario",type(DB.user_name[1]))

# Se inicializan valores
usuarios = {}
for usuario in list(set(DB["user_name"].values)):
  usuarios[usuario] = 0

# Se cuentas los tweets por usuario
for user_name in DB["user_name"].values:
  usuarios[user_name] += 1

# se obtiene el usuario que hizo más tweets
usuarioMax = max(usuarios,key=lambda i: usuarios[i])
print(usuarioMax,"total de tweets= {}".format(usuarios[usuarioMax]))

#Hacemos top 10
print("se hace top 10:")
for i in range(10):
  usuarioMax = max(usuarios,key=lambda i: usuarios[i])
  print("#{}".format(i+1),usuarioMax,"total de tweets= {}".format(usuarios[usuarioMax]))
  usuarios.pop(usuarioMax)  
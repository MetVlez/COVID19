#Crea una función que se encargue de mostrar cuántos tweets por ciudad han sido publicados

import csv
import pandas as pd
from datetime import datetime
from operator import attrgetter

DB = pd.read_csv("covid19_tweets.csv")
print("Las columnas son",DB.keys())
print(DBu[""])
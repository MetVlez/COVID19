from datetime import date
import csv
import math
import pandas as pd
from datetime import datetime


def dias():
    return 0
formato = "%d/%m/%Y"
#primera fecha de un Twitter d1 (año, mes, día)
dia1=datetime.strptime('01/01/2020',formato)
#d2=input('Qué día es hoy? (dd/mm/aaaa)')
dia2=datetime(input('Qué día es hoy? (dd/mm/aaaa)',datetime.strptime(dia2, formato))
diferencia = abs(dia2 - dia1)
print("días transcurridos:", diferencia.days, "días")
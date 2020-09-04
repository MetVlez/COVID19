#días transcurridos.
from datetime import date
import csv
import math
import pandas as pd

def diferencia_dias(d2,d1):
    return abs(d2-d1).days
#primera fecha de un Twitter d1 (año, mes, día)
d1=date(2020,1,1)
#día actual(año, mes, día)
d2=date(2020,2,1)
print("días transcurridos:",diferencia_dias(d1,d2),"días")
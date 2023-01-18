import csv
import numpy
from matplotlib import *

with open('generowane.csv') as openFile:
    data = list(csv.reader(openFile, delimiter=','))
    
print(data[:-10])
print(" ")

data = list(filter(None,data))

time = [x[0] for x in data]
val = [x[1] for x in data]

print(time[:10])
print("")

print(val[:10])

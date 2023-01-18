import random
import math
import csv

from itertools import tee

time = []
data = []
first, _ = tee(data)

for i in range(100):
    time.append(i)
    data.append((math.sin(i) + random.uniform(-0.5,0.5), i + random.random() * math.sqrt(i)))
    
with open('generowane.csv','w') as saveFile:
    saver = csv.writer(saveFile)
    saver.writerows([(time[i], data[i]) for i in range(100)])
    
print(data[0])
print(time[0])

print(next(first))
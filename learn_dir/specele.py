import numpy as np

arr = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(arr)

# [row/col] # start 0 - > ..
print("Get value from 1 row and 5 column -> ",arr[1,5])
# or arr[1,-2] the same result

print(arr[0,:])
# specific row

# [ 1rows, startindex:endindex:stepsize]
print(arr[0,1:6:2])

# 2 rows and 6 columns from 0 to ley
arr[1,5] = 20
print(arr)
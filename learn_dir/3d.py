import numpy as np 

# 3D arr

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(" ")

print("GET VALUE 4 => ",b[0,1,1])

print(".REPLACES.")

# replace values
b[:,1,:] = [[10,10],[11,11]]
print(b)
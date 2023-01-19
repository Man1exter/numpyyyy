import numpy as np

ou = np.ones((5,5))
print(ou)
print(" ")

z = np.zeros((3,3))
z[1,1] = 9
print(z)
print(' ')

ou[1:-1,1:-1] = z
print(ou)
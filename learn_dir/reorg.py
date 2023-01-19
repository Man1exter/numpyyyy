import numpy as np

# a - before / b - after
a = np.array([[1,2,3],[4,5,6]])
print(a)
print("RESHAPED ARRAY")

b = a.reshape((3,2))
print(b)
print(' ')


c1 = np.array([1,2,3,4])
c2 = np.array([1,2,3,4])
print(np.vstack([c1,c2])) #[c1,c2,c1,c2] accept
print(" ")

v1 = np.ones((2,4))
v2 = np.zeros((2,2))
v3 = np.hstack((v1,v2))
print(v3)
print(" ")
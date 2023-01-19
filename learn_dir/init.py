import numpy as np

a = np.zeros(5)
print(a)
print(" ")

b = np.zeros((2,3))
print(b)
print(" ")

c = np.ones((3,2,1))
print(c)
print(" ")

d = np.full((2,2), 69)
print(d)
print(" ")

e = np.random.rand(4,2)
print(e)
print(" ")

f = np.random.randint(7, size=(3,3))
print(f)
print(" ")

g = np.random.randint(2,7, size=(3,3))
print(g)
print(" ")

h = np.array([1,2,3])
h1 = np.repeat(h,5)
print(h1)
print(" ")

i = np.array([[1,2,3]])
i1 = np.repeat(i,5, axis=0)
print(i1)
print(" ")
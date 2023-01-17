import numpy as np


# Tworzenie tablicy: #

# tworzenie tablicy z listy
a = np.array([1, 2, 3])

# tworzenie tablicy zer
b = np.zeros((2,2))

# tworzenie tablicy jedynek
c = np.ones((3,3))

# tworzenie tablicy z krokiem
d = np.arange(0, 10, 2)


# Zmiana rozmiaru tablicy: #

# tworzenie tablicy 2x3
e = np.array([[1, 2, 3], [4, 5, 6]])


# zmiana rozmiaru tablicy na 3x2
f = e.reshape(3,2)

# Operacje na tablicach: #

# tworzenie dwóch tablic
g = np.array([1, 2, 3])
h = np.array([4, 5, 6])

# dodawanie tablic
i = g + h

# mnożenie tablic
j = g * h

# mnożenie skalarne
k = g * 2


# Indeksowanie i wycinanie tablic: #

# tworzenie tablicy
l = np.array([1, 2, 3, 4, 5, 6])

# pobieranie elementu o indeksie 3
m = l[3]

# wycinanie fragmentu tablicy
n = l[1:4]


# Statystyka: #

# tworzenie tablicy
o = np.array([1, 2, 3, 4, 5, 6])

# obliczanie średniej
p = np.mean(o)

# obliczanie odchylenia standardowego
q = np.std(o)
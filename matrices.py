import numpy as np

while True:
    try:
        n, m = map(int, input("Podaj wymiary macierzy (n m): ").split())

        print("Podaj elementy macierzy:")
        elements = []
        for i in range(n):
            row = list(map(int, input().split()))
            elements.append(row)

        a = np.array(elements)

        print("Macierz A:")
        print(a)

        at = np.transpose(a)
        print("Macierz transponowana A^T:")
        print(at)

        ai = np.linalg.inv(a)
        print("Macierz odwrotna A^-1:")
        print(ai)

        ad = np.linalg.det(a)
        print("Wyznacznik macierzy det(A):")
        print(ad)
        break

    except ValueError:
        print("Błędne dane, podaj liczby całkowite")
    except np.linalg.LinAlgError:
        print("Macierz odwrotna nie istnieje, det(A) = 0.")
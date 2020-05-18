import numpy as np
import math

# ZADANIE 1
matrix_1 = np.array([10, 20, 30]).reshape(1, 3)
matrix_2 = np.array([1, 2, 3]).reshape(1, 3)
matrix_dot = matrix_1 * matrix_2
print(matrix_dot)

# ZADANIE 2
m_2_1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90]).reshape(3, 3)
m_2_2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]).reshape(4, 4)
print(m_2_1)
print(m_2_2)
print("Najniższe wartości każdej kolumny w macierzy nr. 1: " + str(m_2_1.min(axis=0)))
print("Najniższe wartości każdym wierszu w macierzy nr. 1: " + str(m_2_1.min(axis=1)))
print("Najniższe wartości każdej kolumny w macierzy nr. 2: " + str(m_2_2.min(axis=0)))
print("Najniższe wartości każdym wierszu w macierzy nr. 2: " + str(m_2_2.min(axis=1)))

# ZADANIE 3
try:
    matrix_3_1 = np.array([10, 20, 30]).reshape(1, 3)
    matrix_3_2 = np.array([1, 2, 3]).reshape(1, 3)
    print(np.dot(matrix_3_1, matrix_3_2))
except ValueError:
    print('Nieprawidłowa wielkość macierzy')

# ZADANIE 4
matrix_1 = np.array([10, 20, 30]).reshape(1, 3)
matrix_2 = np.array([1.11, 2.22, 3.33]).reshape(1, 3)
matrix_dot = matrix_1 * matrix_2
print(matrix_dot)

# ZADANIE 5
matrix_5_1 = np.array([math.radians(30), math.radians(60), math.radians(90), math.radians(120), math.radians(150),
                       math.radians(180)]).reshape(2, 3)
a = np.sin(matrix_5_1)
print(a)

# ZADANIE 6
matrix_6_1 = np.array([math.radians(30), math.radians(60), math.radians(90), math.radians(120), math.radians(150),
                       math.radians(180)]).reshape(2, 3)
b = np.cos(matrix_6_1)
print(b)


# ZADANIE 7
def sum_matrix(m_1, m_2):
    return m_1 + m_2


matrix_5_1 = np.array([math.radians(30), math.radians(60), math.radians(90), math.radians(120), math.radians(150),
                       math.radians(180)]).reshape(2, 3)
matrix_6_1 = np.array([math.radians(30), math.radians(60), math.radians(90), math.radians(120), math.radians(150),
                       math.radians(180)]).reshape(2, 3)
print(sum_matrix(matrix_5_1, matrix_6_1))

# ZADANIE 8
m_8_1 = np.arange(9).reshape(3, 3)
print(m_8_1)
for x in m_8_1:
    print(x)

# ZADANIE 9
m_9_1 = np.arange(9).reshape(3, 3)
print(m_9_1)
for x in m_9_1.flat:
    print(x)

# ZADANIE 10
m_10_1 = np.arange(81).reshape(9, 9)
for x in range(1, 82):
    for y in range(1, 82):
        try:
            m_10_1.reshape(x, y)
        except ValueError:
            print("Z tych wartosci nie mozna zmienic ksztaltu macierzy 9x9: " + str(x) + ', ' + str(y))
        else:
            print('\n' + 'X: ' + str(x) + ' Y: ' + str(y) + '\n' + str(m_10_1.reshape(x, y)) + '\n')
print("Możliwości zmiany kształtu macieży 9x9 to  1x81, 81x1, 3x27, 27x3, ponieważ aby zmienić kształt macieży musi "
      "miećona identyczną liczbę komurek co dają tylko powyższe macieże")

# ZADANIE 11
m_11_1 = np.arange(12).reshape(3, 4).ravel()
m_11_2 = np.arange(12).reshape(4, 3).ravel()
m_11_3 = np.arange(12).reshape(2, 6).ravel()
print(m_11_1, m_11_2, m_11_3)

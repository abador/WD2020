import numpy as np

# # ZADANIE 1
# a = np.array([x for x in range(20*2) if x % 2 == 0])
# print(a)
# print(type(a))

# # ZADANIE 2
# tab = np.arange(10, dtype = 'float')
# print(tab)
# print(tab.dtype)
# tab = tab.astype('int64')
# print(tab)
# print(tab.dtype)

# # ZADANIE 3
# def foo3(n):
#     tab = []
#     for x in range(1, n+1):
#         y = np.array([z for z in range(((x - 1) * n) + 1, (x * n) + 1)])
#         tab.append(y)
#     return np.asarray(tab)
#
# print(foo3(5))

# # ZADANIE 4
# def foo4(x, n):
#     tab = np.arange(n)
#     for y in range(n):
#         tab[y] = pow(x, y+1)
#     return tab
#
# print(foo4(5, 5))

# # ZADANIE 5
# def foo5(n):
#     return np.diag([n-a for a in range(n)])
#
# print(foo5(7))

# # ZADANIE 6
# tab = np.array([np.array(['S', 'A', 'G']), np.array(['I', 'A', 'I']), np.array(['L', 'O', 'L'])])
# print(tab)

# ZADANIE 7
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
#
# Przy założeniach:
# - funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza
# wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.

def foo7(n):
    tab_temp = []
    tab = np.zeros((n, n))
    for z in range(n):
        y = np.array([np.diag([2 * (z + 1) for x in range(n-z)], z)])
        tab_temp.append(y)
        if z != 0:
            y = np.array([np.diag([2 * (z +1) for x in range(n-z)], -z)])
            tab_temp.append(y)
    tab_temp = np.asarray(tab_temp)
    for x in range((2 * n) -1):
        for y in range(n):
            for z in range(n):
                if tab_temp[x][0][y][z] > 0:
                    tab[y][z] = tab_temp[x][0][y][z]

    return tab.astype('int64')

print(foo7(3))
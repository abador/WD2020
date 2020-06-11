import numpy as np

# ZADANIE 1
a = np.array([x for x in range(20 * 2) if x % 2 == 0])
print(a)
print(type(a))

# ZADANIE 2
tab = np.arange(10, dtype='float')
print(tab)
print(tab.dtype)
tab = tab.astype('int64')
print(tab)
print(tab.dtype)


# ZADANIE 3
def foo3(n):
    tab = []
    for x in range(1, n + 1):
        y = np.array([z for z in range(((x - 1) * n) + 1, (x * n) + 1)])
        tab.append(y)
    return np.asarray(tab)


print(foo3(5))


# ZADANIE 4
def foo4(x, n):
    tab = np.arange(n)
    for y in range(n):
        tab[y] = pow(x, y + 1)
    return tab


print(foo4(5, 5))


# ZADANIE 5
def foo5(n):
    return np.diag([n - a for a in range(n)])


print(foo5(7))

# ZADANIE 6
tab1 = list(input())
tab2 = list(input())
tab3 = list(input())
tab_len = [len(tab1), len(tab2), len(tab3)]
tab_len.sort()
tab_len.reverse()
print(tab_len[0])
m = np.array([np.arange(tab_len[0] + 1) for x in range(tab_len[0] + 1)])
m = m.astype('unicode_')
for x in range(1, tab_len[0] + 1):
    if x <= len(tab1):
        m[0][x] = tab1[x - 1]
    if x <= len(tab2):
        m[x][0] = tab2[x - 1]
    if x <= len(tab3):
        m[x][x] = tab3[x - 1]
print(m)


# ZADANIE 7
def foo7(n):
    tab_temp = []
    tab = np.zeros((n, n))
    for z in range(n):
        y = np.array([np.diag([2 * (z + 1) for x in range(n - z)], z)])
        tab_temp.append(y)
        if z != 0:
            y = np.array([np.diag([2 * (z + 1) for x in range(n - z)], -z)])
            tab_temp.append(y)
    tab_temp = np.asarray(tab_temp)
    for x in range((2 * n) - 1):
        for y in range(n):
            for z in range(n):
                if tab_temp[x][0][y][z] > 0:
                    tab[y][z] = tab_temp[x][0][y][z]

    return tab.astype('int64')


print(foo7(3))


# ZADANIE 8
def wypelnianie_tablicy(x, y):
    tablica = np.empty((x, y))
    for x1 in range(x):
        for y1 in range(y):
            tablica[x1, y1] = int(input("Podaj liczbę: "))
    return tablica


def foo8(tablica, kierunek):
    if kierunek.lower() == 'poziomo':
        if tablica.shape[0] % 2 == 0:
            tablica = tablica[:int(tablica.shape[0] / 2)]
            return tablica.astype('int64')
    elif kierunek.lower() == 'pionowo':
        if tablica.shape[1] % 2 == 0:
            tablica = tablica[:, :int(tablica.shape[1] / 2)]
            return tablica.astype('int64')


while True:
    try:
        x = input("Podaj ilość rzędów: ")
        y = input("Podaj ilość kolumn: ")
        z = wypelnianie_tablicy(int(x), int(y))
        kierunek = input("Podaj kierunek [POZIOMO / PIONOWO]: ")
        if kierunek.lower() == 'poziomo' or kierunek.lower() == 'pionowo':
            break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
print(foo8(z, kierunek))


# ZADANIE 9
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


lista = []
for x in range(25):
    lista.append(fibonacci(x + 1))
lista = np.array(lista)
lista = lista.reshape((5, 5))
print(lista)

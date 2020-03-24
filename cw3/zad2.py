import random
random.seed()
macierz = [[random.randint(1, 15) for y in range(4)] for x in range(4)]
print(macierz)
#sposob normalny
for x in range(0, 4):
    for y in range(0, 4):
        if(x==y):
            print(macierz[x][y])
#sposob python comprehension
lista = [macierz[x][y] for x in range (0, 4) for y in range(0, 4) if x==y]
print(lista)
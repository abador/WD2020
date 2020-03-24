def mon(a):
    if a > 0:
        print('Funkcja jest rosnąca')
    elif a < 0:
        print('Funkcja jest malejąca')
    elif a == 0:
        print('Funkcja jest stała')

a = int(input('Podaj wspolczynnik a funkcji liniowej: '))
mon(a)
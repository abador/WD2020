def suma(a1=1, r=1, ile=10):
    return ((2*a1+(ile-1)*r)/2)*ile
a1 = int(input('Podaj a1'))
r = int(input('Podaj r'))
ile = int(input('Podaj ilosc wyrazow ciagu'))
print('Suma wynosi: ', suma(a1, r, ile))
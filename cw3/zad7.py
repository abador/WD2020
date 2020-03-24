import math
def pit(a=0, b=0):
    return a**2+b**2
a = float(input('Podaj pierwszy bok: '))
b = float(input('Podaj drugi bok: '))
print('Dlugosc przeciwprostokatnej wynosi: ', pit(a,b))
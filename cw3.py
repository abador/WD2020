import random
from math import *

#cw1
A=[1/x for x in range(1,11,1)]
print(A)
B=[2**x for x in range(0,11,1)]
print(B)
C=[x for x in B if(x%4==0)]
print(C)
print("\n")
#cw2
macierz = [[random.randint(0,9) for j in range(0,4,1)] for i in range(0,4,1)]
przekatna = [macierz[i][j] for i in range(0,4,1) for j in range(0,4,1) if i==j]
print("Macierz: ")
print(macierz[0])
print(macierz[1])
print(macierz[2])
print(macierz[3])
print("Przekatna macierzy: ",przekatna)
print("\n")
#cw3
produkt_jednostka={
    'ziemniaki': 'kg',
    'piwo': 'butelki',
    'whisky': 'butelki',
    'obóz': 'żydzi'
}
print("Słownik bez odwrócenia: ",produkt_jednostka)
jednostka_produkt = {value: key for key, value in produkt_jednostka.items()}
print("Słownik po odwróceniu: ",jednostka_produkt)
print('\n')
#cw4
def badanie_monotonicznosci(a):
    if a>0:
        return 'rosnaca'
    elif a<0:
        return 'malejaca'
    else:
        return 'stala'

print("Podaj współczynniki a i b funkcji liniowej o wzorze ogolnym y = ax + b")
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
print('Funkcja y='+str(a)+'x+'+str(b)+' jest '+str(badanie_monotonicznosci(a)))
print('\n')
#cw5
def rownolegle_prostopadle(a1,a2):
    if a1==a2:
        return 'rownolegle'
    if (a1*a2==-1):
        return 'prostopadle'
    else:
        return 'ani rownolegle, ani prostopadle'

print("Podaj współczynniki a i b dwóch funkcji liniowych o wzorze ogolnym y = ax + b")
print('Pierwsza funkcja liniowa:')
a1=float(input("Podaj a: "))
b1=float(input("Podaj b: "))
print('Druga funkcja liniowa:')
a2=float(input("Podaj a: "))
b2=float(input("Podaj b: "))
print('y1='+str(a1)+'x+'+str(b1))
print('y2='+str(a2)+'x+'+str(b2))
print('y1 i y2 są '+rownolegle_prostopadle(a1,a2))
print('\n')
#cw6
def okrag(a=0,b=0,x=0,y=0):
    return ((x-a)**2+(y-b)**2)**0.5

print("Współrzędne środka okręgu to (a,b)")
a=float(input('Podaj współrzędną a: '))
b=float(input('Podaj współrzędną b: '))
print("Współrzędne punktu należacego do okręgu to (x,y)")
x=float(input('Podaj współrzędną x: '))
y=float(input('Podaj współrzędną y: '))
print('Długość promienia okręgu to:'+str(okrag(a,b,x,y)))
print('\n')
#cw7
def pitagoras(a=0,b=0):
    return sqrt(a**2+b**2)
print('Podaj długości przyprostokątnych: ')
a= float(input('Podaj pierwsza przyprostokątną: '))
b= float(input('Podaj druga przyprostokątną: '))
print('Przeciwprostokątna wynosi:'+str(pitagoras(a,b)))
print('\n')
#cw8
def suma_arytmetycznego(a1=1,r=1,ile=10):
    return (ile*(2*a1+(ile-1)*r))/2
a1=float(input('Podaj pierwszy wyraz ciagu: '))
r=float(input('Podaj wielkość różnicy miedzy wyrazami ciągu: '))
ile=float(input('Podaj ile wyrazów tego ciagu ma być zsumowanych:'))
print('suma wynosi: '+str(suma_arytmetycznego(a1,r,ile)))
print('\n')
#cw9
def ciag(*liczby):
    if len(liczby)==0:
        return 0.0
    else:
        iloczyn=1.0
        for i in liczby:
            iloczyn*=i
        return iloczyn

print(ciag())
print(ciag(1,2,3,4,5))
print('\n')
#cw10
def ilosc(**zakupy):
    suma=0.0
    for i in zakupy:
        suma = suma + float(zakupy[i])
    return suma
print('liczba wszystkich produktow: ',ilosc(ziemniaki=5, wodka=10, piwo=10, kielbasa=10))
print('\n')

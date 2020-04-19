#Cwiczenie 3 Kacper Walczak
from math import *
#zad1
A=[1/(x+1) for x in range(10)]
B=[2**i for i in range(11)]
C=[x for x in B if x%4==0]
#zad 2
from random import randint,seed
seed(1)
macierz=list()
for i in range(4):
    linia=list()
    for j in range(4):
        linia.append(randint(1,10))
    macierz.append(linia)

print(macierz)
print(macierz[0][0])
print(macierz[1][1])
print(macierz[2][2])
print(macierz[3][3])
przekatna={macierz[i][i] for i in range(4)}
#zad4
def monotonicznosc(a):
    if(a>0):
        print("Funkcja rosnaca")
    elif(a<0):
        print("Funkcja Malejaca")
    else:
        print("Funkcja stała")
monotonicznosc(5)
#zad5
def proste(a1,a2):
    if(a1==a2):
        print("Proste sa rownolegle\n")
    elif(a1*a2==-1):
        print("Proste sa prostopadle\n")
    else:
        print("Proste nie sa ani rownolegle ani prostopadle")
proste(1,-1)
#zad6
def okrag(x,y,a=1,b=1):
    r=pow((x-a),2)+pow((y-b),2)
    print("Promien okregu- ",sqrt(r))
okrag(10,20)
#zad7
def pitagoras(a=0,b=0):
    if(a==0 or b==0):
        print("Bledne dane")
    else:
        c=sqrt(pow(a,2)+pow(b,2))
        print("Przeciwprostokatna - ",c)
pitagoras(3,4)
#zad8
def suma_ciagu(a=1,r=1,n=10,):
    wynik=(((2*a)+(pow((n-1),r)))/2)*n
    print(wynik)
suma_ciagu(1,5)
#zad9
def iloczyn_ciagu(*liczby):
    if(len(liczby)==0):
        return 0.0
    else:
        wynik=1.0
        for i in liczby:
            wynik*=i
        return wynik
print(iloczyn_ciagu())
print(iloczyn_ciagu(1,2,3))
#zad10
def zakupki(**produkty):
    x=0
    for cos in produkty:
        print(cos," kupic ",produkty[cos])
        x+=int(produkty[cos])
    print("w sumie kupisz ",x," sztuk produktow")
zakupki(jajka="10",mleko="3",banany="4")

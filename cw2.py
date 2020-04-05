#Cwiczenie 2 Kacper Walczak
import sys
from math import *
#zad1
x=input("towje spacje w zdaniu: \n")
print(x)
print("iczba spacji- ",x.count(" "))
#zad2
print("podaj dwie liczby")
x=sys.stdin.readline()
y=sys.stdin.readline()
sys.stdout.write(str(int(x)*int(y)))
#zad3
print("operatory- ==, !=, <, >, >=, <=")
#zad4
print("podaj liczbe")
x=sys.stdin.readline()
x=int(x)
print(abs(x))
#zad5
print("podaj trzy liczby")
a=sys.stdin.readline()
b=sys.stdin.readline()
c=sys.stdin.readline()
a=int(a)
b=int(b)
c=int(c)
if a>0 and a<10 and (a>b or b>c):
    print("Warunki sa spelnione")
else:
    print("warunki nie sa spelnione")
# zad6
a = input("podaj liczbe a program wypisze wszytskie liczby podzielne przez 5 do te liczby")
a = int(a)
for x in range(5, a + 1, 5):
    print(str(x) + " ")
#zad7
lista=input("podaj liczby bez odstepow i przecinkow a zobaczysz ich kwadraty jezeli chcesz")
lista=list(lista)
for i in lista:
    wynik=int(i)*int(i)
    print(str(wynik)+" ")
#zad8
#poległemdzis z=input("podaj element listy")
#while(z[len(z)-1]==0):
 #   z.append(input("podaj kolejny element"))
 #zad9
x = input("podaj liczbe wielocyfrowa:")
z = len(x)
wynik = 0
while (z > 0):
    wynik = wynik + int(x[z - 1])
    z = z - 1
    continue
print(wynik)
#zad10
x = input("podaj liczbe mniejsza badz rowna 10:")
x=int(x)
wynik=""
if x>10:
    print("liczba wieksza od 10")

else:
    while(x>0):
        wynik=wynik+"A"
        print(wynik)
        x=x-1


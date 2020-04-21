import sys
print("\n-----cw1-----\n")

#cw1
zadanie=input('Napisz zdanie: \n')
print('W twoim zdaniu jest',zadanie.count(' '),'spacji')

print("\n-----cw2-----\n")

#cw2
import sys
print('Podaj pierwszą wartość: ')
a=sys.stdin.readline()
print('Podaj drugą wartość: ')
b=sys.stdin.readline()
sys.stdout.write('wynik to:' +str(float(a)*float(b)))

print("\n-----cw3-----\n")

#cw3
print('Lista operatorów w instrukcjach warunkowych')
print('Równe: a == b')
print('Różne: a != b')
print('Mniejsze: a < b')
print('Mniejsze bądź równe: a <= b')
print('Większe: a > b')
print('Większe bądź równe: a >= b')

print("\n-----cw4-----\n")

#cw4
from math import *
liczba=input('Podaj liczbe: \n')
liczba=int(liczba)
print('Wartość bezwględna z twojej liczby to',fabs(liczba))

print("\n-----cw5-----\n")

#cw5
a=int(input('Podaj liczbe a: '))
b=int(input('Podaj liczbe b: '))
c=int(input('Podaj liczbe c: '))
if a>0 and a<=10:
    print("liczba a należy do przedziału <0,10>")
else:
    print('liczba a nie nalezy do przedziału <0,10>')
if a>b or b>c:
    print('a>b lub b>c')
else:
    print('a<b lub b<c')

print("\n-----cw6-----\n")

#cw6
print('Liczby podzielne przez 5 od 0 do 300 to: ')
for licznik in range(0, 301, 5):
    print(str(licznik)+' ')

print("\n-----cw7-----\n")

#cw7
lista=[]
for petla in range(1, 5, 1):
    liczba=input('Podaj liczbe: ')
    lista.append(int(liczba))
for petla in range(0, 4, 1):
    print(str(lista[petla]) + '^2 = ' + str(lista[petla]**2))

print("\n-----cw8-----\n")

#cw8
lista=[]
i=0
while i<5:
    liczba = input('Podaj liczbe: ')
    lista.append(int(liczba))
    i+=1
print(lista)

print("\n-----cw9-----\n")

#cw9
liczba=int(input('Podaj liczbe wielocyfrowa: '))
suma=0
while (liczba != 0):
    suma = suma + liczba % 10
    liczba = liczba // 10
print('Suma cyfr wynosi: ' +str(suma))

print("\n-----cw10-----\n")

#cw10
x=int(input('Podaj wysokość wieży, ale nie więcej niż 10: '))
if x>10:
    print('Nie wiecej niz 10!')
    sys.exit(0)
for i in range(0, x, 1):
    for j in range(0, i+1, 1):
        print('A', end='')
    print()




import sys
import math

# ZADANIE 1
napis = input("Podaj zdanie: ")
print(napis.count(' '))

# ZADANIE 2
print('Podaj X: ')
x = sys.stdin.readline()
print('Podaj Y: ')
y = sys.stdin.readline()
wynik = int(x) * int(y)
sys.stdout.write(str(wynik))

# ZADANIE 3 nie wymaga pisania kodu

# ZADANIE 4
n = int(input("Podaj liczbę: "))
print("Wartość bezwzględna z " + str(n) + " to: " + str(math.fabs(n)))

# ZADANIE 5
a = int(input("Podaj A: "))
b = int(input("Podaj B: "))
c = int(input("Podaj C: "))
if 0 < a <= 10 and  (a > b or b > c):
    print("Warunki są spełnione")
else :
    print("Warunki nie są spełnione")

# ZADANIE 6
for x in range(5, 5*11, 5):
    print(x)

# ZADANIE 7
while True:
    x = int(input("Podaj liczbę: "))
    if x == 0 :
        break
    else:
        print(pow(x,2))

# ZADANIE 8
lista = []
print('Program odczytuje liczby od użytkownika i umieszcza je w tablicy.')
while True:
    x = int(input('Podaj liczbę do umieszczenia jej na liśćie: '))
    lista.append(x)
    print('Lista po zmianach ' + str(lista))
    q = str(input('Jeżeli chcesz opuścić program EXIT: '))
    if q == 'EXIT':
        break
print('Koniec programu')

# ZADANIE 9
def suma(x):
    wynik = 0
    while x > 0:
        wynik += x % 10
        x //= 10
    return wynik
liczba = int(input('Podaj liczbę: '))
print("Suma cyfr w liczbie: " + str(suma(liczba)))

# ZADANIE 10
n = int(input('Podaj jaką wysokość ma mnieć wieża ale nie więcej niż 10: '))
if  10 < n or n < 1:
    print('Nieprawidłowe dane wejściowe')
else:
    x = 1
    for i in range(0, n, 1):
        for j in range(0, x, 1):
            sys.stdout.write('H')
        sys.stdout.write('\n')
        x += 1

# ZADANIE 11
while True :
    n = int(input('Podaj liczbę nieparzystą: '))
    if n % 2 == 1 :
        break
for i in range(0, n, 1):
    for j in range(0, n, 1):
        if math.fabs(i - math.floor(n/2)) + math.fabs(j - math.floor(n/2)) <= math.floor(n/2):
            sys.stdout.write('o')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')

# ZADANIE 12
for i in range(1, 101, 1):
    for j in range(1, 101, 1):
        if i * j <10:
            sys.stdout.write('    ')
        elif i * j < 100:
            sys.stdout.write('   ')
        elif i * j < 1000:
            sys.stdout.write('  ')
        elif i * j < 10000:
            sys.stdout.write(' ')
        sys.stdout.write(str(i * j) + ' ')
    print('\n')

# ZADANIE 13 nie wymaga pisania kodu

# ZADANIE 14
while True:
    n = input("Podaj liczbę: ")
    if n > str(0):
        break
pierwiastek = math.sqrt(float(n))
print(pierwiastek)

# ZADANIE 15
n = input('Podaj liczbę: ')
for i in range(0, len(n), 1):
    if (n[i] >= 'a' or 'z' <= n[i]) or (n[i] >= 'A' or 'Z' <= n[i]):
        print('BŁĄD użytkownik podał literę zamiast cyfry')
        break

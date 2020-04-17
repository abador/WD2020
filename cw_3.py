# import math
# import random
#from liczby_zespolone import dodawanie_odejmowanie, urojona_rzeczywista
#
# # ZADANIE 1
# A = [1 / x for x in range(1, 11, 1)]
# B = [2 ** x for x in range(11)]
# C = [x for x in B if x % 4 == 0]
# print(A)
# print(B)
# print(C)
#
# # ZADANIE 2
# random.seed()
# A = [[random.randint(1,10) for i in range(4)] for j in range(4)]
# lista = [A[i][j] for i in range(4) for j in range(4) if i == j]
# print(A)
# print(lista)
#
# # ZADANIE 3
# produkty = {"Sok": 'Sztuka',
#             "Woda": "Sztuka",
#             "Chips": "Kilogram",
#             "Płatki" : "Kilogram",
#             "Pizza" : "Sztuka"}
# lista = [x for (x, y) in produkty.items() if y == 'Sztuka']
# print(lista)
#
# # ZADANIE 4
# def monotonicznosc(a):
#     if a > 0:
#         print(u"Funkcja liniowa jest rosnąca")
#     elif a < 0:
#         print(u"Funkcja jest malejąca")
#     else:
#         print(u"Funkcja liniowa jest stałą")
#
# print("Dla funkcji linowej w postaci y = ax + b")
# while True:
#     a = input(u"Podaj wartość parametru a: ")
#     b = input(u"Podaj wartość parametru b: ")
#     try:
#         float(a)
#         float(b)
#         monotonicznosc(float(a))
#         break
#     except ValueError:
#         print(u"BŁĄD - Podano niepoprawną wartość")
#
# # ZADANIE 5
# def rownolegle_prostopadle(x, y):
#     if x == y:
#         print(u"Podane proste są równoległe")
#     elif x * y == 1:
#         print(u"Podane proste są prostopadłe")
#
# print(u"Prosta dane równaniem liniowym w postaci y = ax + b")
# while True:
#     a1 = input(u"Podaj wartość parametru a1: ")
#     b1 = input(u"Podaj wartość parametru b1: ")
#     a2 = input(u"Podaj wartość parametru a2: ")
#     b2 = input(u"Podaj wartość parametru b2: ")
#     try:
#         float(a1)
#         float(b1)
#         float(a2)
#         float(b2)
#     except ValueError:
#         print(u"BŁĄD - Podano niepoprawną wartość")
#     finally:
#         rownolegle_prostopadle(float(a1), float(a2))
#         break
# # ZADANIE 6
# def rownanie_okregu_k(x = 0, y = 0, a = 0, b = 0):
#     return math.sqrt(pow(x - a, 2) + pow(y - b, 2))
#
# print("Równanie okręgu określone wzorem: (x - a)^2 + (y - b)^2 = r^2")
# while True:
#     x = input(u"Podaj wartość x dla punktu na okręgu: ")
#     y = input(u"Podaj wartość y dla punktu na okręgu: ")
#     a = input(u"Podaj wartość x dla środka okręgu: ")
#     b = input(u"Podaj wartość y dla środka okręgu: ")
#     try:
#         float(x)
#         float(y)
#         float(a)
#         float(b)
#         break
#     except ValueError:
#         print(u"BŁĄD - Podano niepoprawną wartość")
# print(rownanie_okregu_k(float(x), float(y), float(a), float(b)))
#
# # ZADANIE 7
# def pitagoras(a = 0, b = 0):
#     print(math.sqrt(pow(a, 2) + pow(b, 2)))
#
# print("Twierdzenie Pitagorasa określone wzorem a^2 + b^2 = c^2")
# while True:
#     a = input(u"Podaj wartość a: ")
#     b = input(u"Podaj wartość b: ")
#     try:
#         float(a)
#         float(b)
#         break
#     except ValueError:
#         print(u"BŁĄD - Podano niepoprawną wartość")
# pitagoras(float(a), float(b))
#
# #ZADANIE 8
# def c_arytmetyczny(a = 1.0, b = 1.0, c = 10):
#     suma = a
#     for i in range(1, c):
#         suma += i*b+a
#     return round(suma, 2)
# print(u"Ciąg arytmetyczny")
# while True:
#     x = input(u"Podaj wartość a1: ")
#     y = input(u"Podaj wartość o ile rosną kolejne elementy: ")
#     z = input(u"Podaj ile elementów ciągu ma być sumowanych: ")
#     try:
#         float(x)
#         float(y)
#         int(z)
#         break
#     except ValueError:
#         print(u"BŁĄD - Podano niepoprawną wartość")
# print(c_arytmetyczny(float(x), float(y), int(z)))
#
# # ZADANIE 9
# def ciag(* liczby):
#     if len(liczby) == 0:
#         return 0.0
#     else:
#         suma = 1.0
#         for i in liczby:
#             suma *= float(i)
#         return suma
# # Jak wczytywać krotki
# # 1 - zaimplementowany
# # 2
# # tuple(int(x.strip()) for x in raw_input().split(','))
# # Jak konwertować listę na krotkę
# print(u"Podaj wartości stosując jako separator spację: ")
# while True:
#     t = tuple(x.strip() for x in input().split(' '))
#     try:
#         for i in range(len(t)):
#             float(t[i])
#         break
#     except ValueError:
#         print(u"BŁĄD - Podano niepoprawną wartość")
#     finally:
#         for i in range(len(t)):
#             float(t[i])
# print(ciag(*t))
#
# # ZADANIE 10
# def to_lubie(** lista):
#     global suma_produktow
#     for ilosc in lista:
#         suma_produktow += lista[ilosc]
#     print(suma_produktow)
# print('LISTA ZAKUPÓW')
# suma_produktow = 0
# ile_razy = int(input("Podaj ile produktów ma być dodanych na listę zakupów: "))
# while True:
#     for x in range(ile_razy):
#         produkt = input(u'Podaj nazwę produktu jaki chcesz dodać do listy zakupów: ')
#         n = int(input(u"Podaj ile chcesz dodać elementów do listy zakupów: "))
#         to_lubie(produkt = n)
#     powtorka = input(u"Jeżeli chcesz dodać coś jeszcze do listy wpisz 'TAK: ")
#     if 'tak' != powtorka.lower():
#         break
#
# ZADANIE 11
# x = complex(input("Podaj wartość w formacie x+yj gdzie x, y podaje użytkownik: "))
# z = urojona_rzeczywista.rzeczywista(x)
# print(z)
# z = urojona_rzeczywista.urojona(x)
# print(z)
# y = complex(input("Podaj wartość w formacie x+yj gdzie x, y podaje użytkownik: "))
# z = dodawanie_odejmowanie.dodawanie(x, y)
# print(z)
# z = dodawanie_odejmowanie.odejmowanie(x , y)
# print(z)

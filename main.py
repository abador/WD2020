import random
from plik import *
from akcje import *


def nowa_gra(point):
    print("\n\nWpisz W,A,S,D aby poruszac sie w danym kierunku\n")
    print("Wpisz Q aby wyjsc oraz Z aby zapisać grę")
    kierunek = input()
    if kierunek == "D" or kierunek == "d":
        vector = {"x": 5, "y": 0}
        funkcje.move(point, vector)
        for key in point:
            print(key + " " + str(point[key]))
        nowa_gra(point)
    if kierunek == "A" or kierunek == "a":
        vector = {"x": -5, "y": 0}
        funkcje.move(point, vector)
        for key in point:
            print(key + " " + str(point[key]))
        nowa_gra(point)
    if kierunek == "W" or kierunek == "w":
        vector = {"x": 0, "y": 5}
        funkcje.move(point, vector)
        for key in point:
            print(key + " " + str(point[key]))
        nowa_gra(point)
    if kierunek == "S" or kierunek == "s":
        vector = {"x": 0, "y": -5}
        funkcje.move(point, vector)
        for key in point:
            print(key + " " + str(point[key]))
        nowa_gra(point)
    if kierunek == "Z" or kierunek == "z":
        print("Czy chcesz podac nazwe save'a? (Inaczej domyslna nazwa bedzie save) 0 - Nie, 1 - Tak")
        wybor = int(input())
        if wybor == 0:
            savegame.save(str(point))
        elif wybor == 1:
            print("Podaj nazwe save")
            nazwa = input()
            savegame.save(str(point), nazwa)
    if kierunek == "Q" or kierunek == "q":
        print("Koncze gre")
        return 0



print("---Rycerz gra---\n")
print("Wybierz opcje\n")
print("1. Nowa gra\n")
print("2. Wczytaj gre\n")
choose = int(input("Twoj wybor"))
if choose == 1:
    print("Zaczynam nowa grę\n")
    point = {"x": random.randint(1, 30), "y": random.randint(1, 30)}
    nowa_gra(point)
if choose == 2:
    print("Podaj nazwe save'a do wczytania")
    try:
        nazwa = str(input())
        point = savegame.load(nazwa)
        point = eval(point)
        nowa_gra(point)
    except FileNotFoundError:
        print("Taki save'a nie istnieje. Try again!")

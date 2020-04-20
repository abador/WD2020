from akcje import *
from plik import *
import random
import time

def start():
    point = {"pozx" : 0, "pozy" : 0}
    point["pozx"] = random.randint(0, 1000)
    point["pozy"] = random.randint(0, 1000)
    return point

def menu():
    with open("menu.txt", "r") as file:
        for x in file:
            print(x, end= "")
    liczba_prob = 3
    while True:
        try:
            a = int(input(u"\nPodaj wartość: "))
            print("----------------")
            return a
            break
        except ValueError:
            print(u"BŁĄD - Podano niepoprawną wartość, należy podać liczbę całkowitą")
            liczba_prob -= 1
            if liczba_prob == 1:
                print(u"Zdecyduj się, bo zaraz kończę")
            elif liczba_prob == 0:
                quit(u"\nA nie mówiłem")

def instrukcja():
    with open("instrukcja.txt", "r") as file:
        for x in file:
            print(x, end= "")

def gra(dict):
    ruch = {"pozx": 0, "pozy": 0}
    while True:
        try:
            print("----------------")
            zmienna = str(input(u"Podaj wartość: "))
            print("----------------")
            if zmienna.lower() == "w" or zmienna.lower() == "a" or zmienna.lower() == "s" or zmienna.lower() == "d" or zmienna.lower() == "q":
                if zmienna.lower() == "w":
                    ruch["pozy"] += 1
                elif zmienna.lower() == "s":
                    ruch["pozy"] -= 1
                elif zmienna.lower() == "a":
                    ruch["pozx"] -= 1
                elif zmienna.lower() == "d":
                    ruch["pozx"] += 1
            if zmienna.lower() == "q" or zmienna.lower() == "quit":
                quit("KONIEC PROGRAMU")
            funkcje.move(dict, ruch)
            if zmienna.lower() == "s" or zmienna.lower() == 'save':
                savegame.save(dict)
                if zmienna.lower() == 'save':
                    print(u"Sukces!\nGra została zapisana")
            ruch = {"pozx": 0, "pozy": 0}
            print("X: " + str(dict["pozx"]) + " Y: " + str(dict["pozy"]))
        except ValueError:
            print(u"BŁĄD - Podano niepoprawną wartość, należy podać liczbę całkowitą")

def nowa_gra():
    print("----------------")
    print(u"Czy aby napewno chcesz zacząć nową grę: ")
    print(u"UWAGA! Nowa gra spowoduje usunięcie zapisanej rozgrywki")
    z = input("TAK / NIE: ")
    print("----------------\n")
    if "tak" == z.lower():
        dict = start()
        print("----------------")
        print("Początkowa pozycja X: " + str(dict["pozx"]))
        print("Początkowa pozycja Y: " + str(dict["pozy"]))
        print("----------------\n")
    elif "nie" == z.lower():
        quit(u"KONIEC PROGRAMU")
    else:
        quit(u"KONIEC, BŁĄD DZIAŁANIA PROGRAMU")
    with open("opis.txt", "r") as file:
        for x in file:
            print(x, end="")
    gra(dict)

def end():
        print(u"Czy aby napewno chcesz opuścić program: ")
        q = input("TAK / NIE: ")
        if "tak" == q.lower():
            quit("KONIEC PROGRAMU")
while True:
    x = menu()

    if x == 1:
        dict = {"pozx" : 0, "pozy" : 0}
        list = savegame.load()
        dict = {"pozx" : list[0], "pozy" : list[1]}
        print("Twoja pozycja to X: " + dict["pozx"] + " Y: " + dict["pozy"])
        with open("opis.txt", "r") as file:
            for x in file:
                print(x, end="")
        gra(dict)

    if x == 2:
        nowa_gra()

    if x == 3:
        instrukcja()
        time.sleep(15)

    if x == 4:
        end()
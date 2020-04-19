from plik import *
from akcje import *
import random

def saveoption():
    file = input("Podaj nazwe pliku do zapisania save'a ")
    savegame.save(file, point)

def options():
    print("===================")
    print("Wybierz opcję:")
    print("1. Wczytaj")
    print("2. Zapisz")
    print("3. Nowa gra")
    print("===================")

def play():
    while True:
        print("Twoja pozycja to: [%(x)d, %(y)d]" % {'x': point["x"], 'y': point["y"]})
        print("Użyj WSAD aby się poruszyć (Q żeby przerwać i wrócić do menu lub H żeby zapisać)")
        litera = input("Podaj litere: ")
        if litera == 'Q' or litera == 'q':
            break
        elif litera == 'H' or litera == 'h':
            saveoption()
            print('Gra została zapisana, graj dalej!')
        elif litera == 'a' or litera == 'A':
            print('Poruszasz się w lewo!')
            vector = {"x" : -1, "y" : 0}
            funkcje.move(point, vector)
        elif litera == 'd' or litera == 'D':
            print('Poruszasz się w prawo!')
            vector = {"x": 1, "y": 0}
            funkcje.move(point, vector)
        elif litera == 'w' or litera == 'W':
            print('Poruszasz się do przodu!')
            vector = {"x": 0, "y": 1}
            funkcje.move(point, vector)
        elif litera == 'S' or litera == 's':
            print('Poruszasz się do tyłu!')
            vector = {"x": 0, "y": -1}
            funkcje.move(point, vector)
        else:
            print("Ta litera jest niepoprawna, podaj inną!")

random.seed()
options()
choose = int(input(""))
point = {"x" : random.randint(1,15), "y" : random.randint(1,15)}
if choose == 1:
    file = input("Podaj nazwe pliku z savem: ")
    savegame.load(file, point)
    play()
elif choose == 3:
    print('Rozpoczynamy nową grę!')
    play()
elif choose == 2:
    saveoption()
    print('Gra została zapisana!')


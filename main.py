import sys
import random
from akcje import *
from plik import *


def start():
    print("Wybierz numer 1, 2 lub 3")
    print("1 Nowa gra \n2 Wczytaj gre\n3 Wyjscie")
    try:
        wybor = int(sys.stdin.readline())
        if wybor == 1:
            pozycja = {'pozx': random.randint(-100, 100), 'pozy': random.randint(-100, 100)}
            return pozycja
        elif wybor == 2:
            print("Wybierz numer pliku z zapisem gry\n1 Zapis pierwszy\n2 Zapis drugi\n3 Zapis trzeci")
            numer = int(sys.stdin.readline())
            if numer == 1 or numer == 2 or numer == 3:
                pozycja = savegame.load(numer)
                return pozycja
            else:
                print("Nie wybrales poprawnego numeru wyboru zapisu gry, powrot do menu glownego")
                start()
        elif wybor == 3:
            print("Wyszedles z gry")
            sys.exit(0)
        else:
            print("Nie wybrales poprawnego numeru wyboru w menu, sprobuj jeszcze raz")
            start()
    except ValueError:
        print("Nie wybrales cyfry, powrot do menu glownego")
        start()


pozycja = start()
print(pozycja)
wgrze = input("WSAD sterowanie, Z zapis, Q wyjscie\n")
while wgrze not in ['Q', 'q']:
    if wgrze in ['W', 'w']:
        przesuniecie = {'pozx': 0, 'pozy': 1}
        funkcje.move(pozycja, przesuniecie)
        wgrze = input("WSAD sterowanie, Z zapis, Q wyjscie\n")
    elif wgrze in ['S', 's']:
        przesuniecie = {'pozx': 0, 'pozy': -1}
        funkcje.move(pozycja, przesuniecie)
        wgrze = input("WSAD sterowanie, Z zapis, Q wyjscie\n")
    elif wgrze in ['A', 'a']:
        przesuniecie = {'pozx': -1, 'pozy': 0}
        funkcje.move(pozycja, przesuniecie)
        wgrze = input("WSAD sterowanie, Z zapis, Q wyjscie\n")
    elif wgrze in ['D', 'd']:
        przesuniecie = {'pozx': 1, 'pozy': 0}
        funkcje.move(pozycja, przesuniecie)
        wgrze = input("WSAD sterowanie, Z zapis, Q wyjscie\n")
    elif wgrze in ['Z', 'z']:
        try:
            numer = int(input(
                "Wybierz numer pliku w ktorym chcesz dokonac zapisu\n1 Zapis pierwszy\n2 Zapis drugi\n3 Zapis trzeci\n"))
            if numer in [1, 2, 3]:
                savegame.save(numer, pozycja)
                print("Gra zostala zapisana")
                wgrze = input("WSAD sterowanie, Z zapis, Q wyjscie\n")
            else:
                print("Nie ma takiego pliku zapisu, gra nie zostala zapisana")
                wgrze = input("WSAD sterowanie, Z zapis, Q wyjscie\n")
        except ValueError:
            print("Nie wybrales cyfry, gra nie zostala zapisana")
            wgrze = input("WSAD sterowanie, Z zapis, Q wyjscie\n")
    else:
        print("Niepoprawny klawisz, spróbuj jeszcze raz")
        wgrze = input("WSAD sterowanie, Z zapis, Q wyjscie\n")

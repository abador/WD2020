def save(numer, pozycja):
    if numer == 1:
        plik = open("save1.py", "w")
    elif numer == 2:
        plik = open("save2.py", "w")
    elif numer == 3:
        plik = open("save3.py", "w")
    plik.write(str(pozycja))
    plik.close()


def load(numer):
    try:
        if numer == 1:
            plik = open("save1.py", "r")
        elif numer == 2:
            plik = open("save2.py", "r")
        elif numer == 3:
            plik = open("save3.py", "r")
        odczytstr = plik.readline()
        plik.close()
        odczyt = eval(odczytstr)
        return odczyt
    except FileNotFoundError:
        print("Nie zapisales gry na tym pliku, rozpoczynanie nowej gry")
        return 0

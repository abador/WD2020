import random

class Objekt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Pobierz_X(self):
        return self.x

    def Pobierz_Y(self):
        return self.y

    def Ruch_X(self, x):
        self.x = x

    def Ruch_Y(self, y):
        self.y = y

class Robaczek(Objekt):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.predkosc = 1
        self.poziom = 1
        self.najedzenie = 0

    def ZjedzOwoc(self, owoc, owoce):
        self.najedzenie += owoc.PobierzJedzenie()
        print('\n    OOO! Zjadłeś owoc, który dał Ci - ' + str(owoc.PobierzJedzenie()) + ' EXP')
        owoce.remove(owoc)

    def SprawdzPoziom(self):
        if self.najedzenie >= 10:
            self.najedzenie -= 10
            self.poziom += 1
            print('    Awansowałeś na LVL ', self.poziom)

class Owoc(Objekt):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.jedzenie = random.randint(1, 5)

    def PobierzJedzenie(self):
        return self.jedzenie

def PobierzOwoce():
    lista = []
    with open('owoce.txt', 'r') as file:
        linie = file.readlines()
        for linia in linie:
            aftersplit = linia.split(',')
            owoc_nowy = Owoc(aftersplit[0], aftersplit[1])
            lista.append(owoc_nowy)
    return lista

def WypiszOwoce(owoce):
    print("\n    ----------------\n")
    for x in range(len(owoce)):
        print("    " + str(x + 1) + ".  X: " + owoce[x].x + '  Y: ' + owoce[x].y + '  Moc: ' + str(owoce[x].jedzenie))
    print("\n    ----------------")

def Start():
    return random.randint(1, 10)

def Sprawdz(robaczek, owoce):
    for owoc in owoce:
        if (int(robaczek.x) == int(owoc.x) and int(robaczek.y) == int(owoc.y)) is True:
            robaczek.ZjedzOwoc(owoc, owoce)
        robaczek.SprawdzPoziom()

def move(x, y, predkosc):
    print(u"\nAktualna pozycja - X: " + str(x) + " Y: " + str(y))
    way = ['w', 'a', 's', 'd']
    direction = input(u"Podaj kierunek, w który chcesz się udać: ")
    if direction.lower() == way[0]:
        if robaczek.y + int(predkosc) > 10:
            print("Nie możesz iść dalej na północ, zawróć!")
        else:
            robaczek.Ruch_Y(robaczek.Pobierz_Y() + int(predkosc))
            Sprawdz(robaczek, owoce)
    elif direction.lower() == way[1]:
        if robaczek.x - int(predkosc) < 1:
            print("Nie możesz iść dalej na zachód, zawróć!")
        else:
            robaczek.Ruch_X(robaczek.Pobierz_X() - int(predkosc))
            Sprawdz(robaczek, owoce)
    elif direction.lower() == way[2]:
        if robaczek.y - int(predkosc) < 1:
            print("Nie możesz iść dalej na połódnie, zawróć!")
        else:
            robaczek.Ruch_Y(robaczek.Pobierz_Y() - int(predkosc))
            Sprawdz(robaczek, owoce)
    elif direction.lower() == way[3]:
        if robaczek.x + int(predkosc) > 10:
            print("Nie możesz iść dalej na wschód, zawróć!")
        else:
            robaczek.Ruch_X(robaczek.Pobierz_X() + int(predkosc))
            Sprawdz(robaczek, owoce)
    elif direction.lower() == 'info':
        print("\n    ----------------")
        print('\n    LVL: ' + str(robaczek.poziom) + '\n    EXP: ' + str(robaczek.najedzenie))
        print("\n    ----------------")
    elif direction.lower() == "owoce":
        WypiszOwoce(owoce)

print("ROBACZEK")
owoce = PobierzOwoce()
WypiszOwoce(owoce)
robaczek = Robaczek(Start(), Start())
print(u"\n    Ruszasz się WASD")
predkosc = input(u"\n    Domyślna i zalecana prędkość wynosi 1, jeżeli chcesz ją zmienić wpisz ją ")
try:
    int(predkosc)
    robaczek.predkosc = predkosc
except ValueError:
    print('    Podałeś coś innego, trudno. To gramy po mojemu')
while len(owoce) is not 0:
    move(robaczek.x, robaczek.y, robaczek.predkosc)
print("\n    ----------------\n\n"
      "    KONIEC GRY - WYGRAŁEŚ\n\n"
      "    LVL - " + str(robaczek.poziom) +
      "\n    EXP - " + str(robaczek.najedzenie) +
      "\n\n    ----------------")
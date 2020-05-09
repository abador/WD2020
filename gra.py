import random


class Obiekt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Robaczek(Obiekt):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.poziom = 1
        self.najedzenie = 0
        self.predkosc = 1

    def zjedzOwoc(self, owoc, lista):
        self.najedzenie += owoc.pobierzJedzenie()
        print('Zjadasz owoc o poziomie najedzenia: ', owoc.pobierzJedzenie())
        print('Twój poziom najedzenia: ', self.najedzenie, '/5')
        lista.remove(owoc)

    def SprawdzPoziom(self):
        if self.najedzenie >= 5:
            self.najedzenie = 5-self.najedzenie
            self.poziom += 1
            print('Awansujesz na poziom ', self.poziom)


class Owoc(Obiekt):
    def __init__(self, x, y):
        super().__init__(x, y)
        random.seed()
        self.jedzenie = random.randint(1, 5)

    def pobierzJedzenie(self):
        return self.jedzenie


def PobierzOwoce(path):
    lista = []
    file = open(path, 'r')
    linie = file.readlines()
    for linia in linie:
        aftersplit = linia.split(' ')
        owocnowy = Owoc(aftersplit[0], aftersplit[1])
        lista.append(owocnowy)
    return lista


def sprawdzPozycje(rob, ow):
    if int(rob.x) == int(ow.x) and int(ow.y) == int(rob.y):
        return True
    return False


def sprawdz(robak, owoce):
    for owoc in owoce:
        if sprawdzPozycje(robak, owoc) is True:
            robak.zjedzOwoc(owoc, owoce)
    robak.SprawdzPoziom()


path = input("Podaj nazwę pliku z współrzędnymi owoców(domyślnie podaj owoce.txt) ")
owoce = PobierzOwoce(path)

x1 = int(input("Podaj współrzędną startową X robaczka: "))
y1 = int(input("Podaj współrzędną startową Y robaczka: "))

robak = Robaczek(x1, y1)

while len(owoce) != 0:
    print("Twoja pozycja to: [%(x)d, %(y)d]" % {'x': robak.getX(), 'y': robak.getY()})
    print("Użyj WSAD aby się poruszyć (Q żeby przerwać, N żeby wyświetlić informację o robaczku)")
    litera = input("Podaj litere: ")
    if litera == 'Q' or litera == 'q':
        break
    elif litera == 'a' or litera == 'A':
        print('Poruszasz się w lewo!')
        robak.setX(robak.getX() - 1)

        sprawdz(robak, owoce)
    elif litera == 'd' or litera == 'D':
        print('Poruszasz się w prawo!')
        robak.setX(robak.getX() + 1)

        sprawdz(robak, owoce)
    elif litera == 'w' or litera == 'W':
        print('Poruszasz się do przodu!')
        robak.setY(robak.getY() + 1)

        sprawdz(robak, owoce)
    elif litera == 'S' or litera == 's':
        print('Poruszasz się do tyłu!')
        robak.setY(robak.getY() - 1)

        sprawdz(robak, owoce)
    elif litera == 'N' or litera == 'n':
        print("Poziom: ", robak.poziom)
        print("Poziom najedzenia: ", robak.najedzenie, "/", '5')
        print("Prędkość: ", robak.predkosc)
    else:
        print("Ta litera jest niepoprawna, podaj inną!")

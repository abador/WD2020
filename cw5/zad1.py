class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj)


class Ubranie(Material):
    def ustawRozmiar(self, rozmiar):
        self.rozmiar = rozmiar

    def ustawKolor(self, kolor):
        self.kolor = kolor

    def ustawDlaKogo(self, dlakogo):
        self.dlakogo = dlakogo

    def wyswietl_dane(self):
        print('Rozmiar: ', self.rozmiar)
        print('Kolor: ', self.kolor)
        print('Dla: ', self.dlakogo)


class Sweter(Ubranie):
    def ustawRodzaj(self, rodzajswetra):
        self.rodzajswetra = rodzajswetra

    def wyswietl_dane(self):
        print('Rodzaj swetra: ', self.rodzajswetra)

bawelna = Material('Bawelna', '2m', '3m')
bawelna.wyswietl_nazwe()


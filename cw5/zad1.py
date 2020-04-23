class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj)


class Ubranie(Material):
    def __init__(self, rodzaj, rozmiar, kolor, dlakogo):
        self.rodzaj = rodzaj
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dlakogo = dlakogo

    def wyswietl_dane(self):
        print('Rozmiar: ', self.rozmiar)
        print('Kolor: ', self.kolor)
        print('Dla: ', self.dlakogo)


class Sweter(Ubranie):
    def __init__(self, rodzaj, rozmiar, kolor, dlakogo, rodzajswetra):
        super().__init__(rodzaj, rozmiar, kolor, dlakogo)
        self.rodzajswetra = rodzajswetra

    def wyswietl_dane(self):
        print('Rodzaj swetra: ', self.rodzajswetra)

bluza = Ubranie('Bawełna', 'S', 'Zielona', 'Grzegorz')
bluza.wyswietl_dane()
bluza.wyswietl_nazwe()

print('    ')

sweter1 = Sweter('Bawełna', 'M', 'Czerwony', 'Adam', 'Z zamkiem')
sweter1.wyswietl_dane()
sweter1.wyswietl_nazwe()





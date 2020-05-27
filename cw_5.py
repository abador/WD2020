# ZADANIE 1
class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj + '\n')

class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print("Rozmiar: " + self.rozmiar + "\nKolor: " + self.kolor + "\nDla kogo: " + self.dla_kogo + "\n")

class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        print("Rodzaj swetra: " + self.rodzaj_swetra + '\n')

Cotton = Material("Bawełna", 10, 1)
Cotton.wyswietl_nazwe()
Wool = Ubrania("XL", "Biały", "Mężczyzna")
Wool.wyswietl_dane()
Silk = Sweter("Golf")
Silk.wyswietl_dane()

# ZADANIE 2
class Ksztalty:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis

    def pole_prostokatu(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, z):
        return Kwadrat(self.x + z)

Cube = Kwadrat(2)
Cube_2 = Cube.__add__(3)
print(Cube_2.x)

# ZADANIE 3
class Ksztalty:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis

    def pole_prostokatu(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, other):
        return Kwadrat(self.x + other)

    def __ge__(self, other):
        return self.x >= other.x

    def __gt__(self, other):
        return self.x > other.x

    def __le__(self, other):
        return self.x <= other.x

    def __lt__(self, other):
        return self.x < other.x

Cube = Kwadrat(2)
Cube_2 = Cube.__add__(1)
print("Cube    " + str(Cube.x))
print("Cube_2  " + str(Cube_2.x))
if Cube.__lt__(Cube_2) is True:
    print('Obiekt Cube ma mniejszy bok')
    print('Obiekt Cube_2 ma większy bok')

else:
    print('Obiekt Cube ma większy bok')
    print('Obiekt Cube_2 ma mniejszy bok')

# ZADANIE 4
class Point:
    counter = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.counter += 3
        print("init: counter = {}".format(self.counter))

p1 = Point(1, 1)
p2 = Point(1, 1)
p2.__init__()
print(p2.x, p2.y, p2.counter)
p1.counter += 1
print(p1.x, p1.y, p1.counter)

# ZADANIE 5
class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

krowa = Wspak("Krowa")
for x in krowa:
    print(x)

# ZADANIE 6
class Nieparzyste:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        if self.index == len(self.data):
            raise StopIteration
        if self.index % 2 == 0:
            return self.data[self.index]

napis = Nieparzyste("napis")
for x in napis:
    print(x)

# Czy jest możliwość aby usyskać wyjście inne niż
# n
# none
# p
# none
# s
# Aby zamiast tego było
# n
# p
# s

# ZADANIE 7
class samogloski:
    def __init__(self, napis):
        self.napis = napis
        self.samogloski = ["a", "ą", "e", "ę", "i", "o", "u", "y", "ó"]
        self.czynapis = isinstance( self.napis, str)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.czynapis is False:
            raise StopIteration
        self.index = self.index + 1
        if self.index == len(self.napis):
            raise StopIteration
        if self.napis[self.index] in self.samogloski:
            return self.napis[self.index]

abecadlo = samogloski("abc")
for x in abecadlo:
    print(x)

# ZADANIE 8
def Nieparzyste(data):
    for index in range(len(data)):
        if index % 2 == 0:
            yield data[index]

napis = Nieparzyste("napis")
for x in napis:
    print(x)

# ZADANIE 9
import itertools
ile = 1
napis = itertools.permutations('0123456789', 3)
for x in napis:
    print(str(ile) + ".     " + str(x))
    ile += 1

# ZADANIE 10
def Fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(Fibonacci(6)))

# ZADANIE 11
miesiace = ["Styczeń", "Luty", "Marzec",
            "Kwiecień", "Maj", "Czerwiec",
            "Lipiec", "Sierpień", "Wrzesień",
            "Październik", "Listopad", "Grudzień"]
miesiac = (x for x in miesiace)
for x in miesiac:
    print(x)

class Ksztalty:
    #definicja konstruktora
    def __init__(self, x, y):
        #deklarujemy atrybuty
        #self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole_prostokatu(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


#a teraz klasa która dziedziczy po klasie Ksztalty
class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, other):
        return Kwadrat(self.x+other)

    def __ge__(self, other):
        return self.x >= other.x

    def __gt__(self, other):
        return self.x > other.x

    def __le__(self, other):
        return self.x <= other.x

    def __lt__(self, other):
        return self.x < other.x



kwadrat1 = Kwadrat(2)
kwadrat2 = kwadrat1+3
print(str(kwadrat2.x))
if kwadrat2 >= kwadrat1:
    print('Obiekt kwadrat1 ma mniejszy/równy bok')
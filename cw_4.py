# ZADANIE 1
lista = [x for x in range(101) if x % 4 == 0]
plik = open("zadanie_4_1.txt", "w")
plik.writelines(str(lista))
plik.close()

# ZADANIE 2
with open("zadanie_4_1.txt", "r+") as plik:
    for x in plik:
        print(x, end="")
print("\n")

# ZADANIE 3
with open('zadanie_4_3.txt', 'w') as plik3:
    plik3.write("Ala ma kota\n")
    ciag = [x for x in range(0, 101, 5)]
    plik3.writelines(str(ciag))
with open("zadanie_4_3.txt", "r") as plik3:
    for x in plik3:
        print(x, end="")
print("\n")

# ZADANIE 4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miasry, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miasry
        self.cena_jed = cena_jed

    def wyświetl_produkt(self):
        print(str(self.nazwa_produktu.capitalize()) + " " + str(self.ilosc) + " " + str(self.jednostka_miary) + " " + str(self.cena_jed) + " " + "zł")

    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        print(str(self.ilosc * self.cena_jed) + " zł")

maslo = NaZakupy("masło", 2, "kostka", 4)
print("----------------")
maslo.wyświetl_produkt()
print("----------------")
maslo.ile_produktu()
print("----------------")
maslo.ile_kosztuje()
print("\n\n")

# ZADANIE 5
class CiagArytmetyczny:
    def wyswietl_dane(self):
        print("a_1:", self.a_1)
        print("r:", self.r)
        print("n:", self.n)

    def pobierz_elementy(self):
        liczba = int(input("Podaj, który element ciągu chcesz obliczyć: "))
        return self.wartosc_ciagu(liczba)

    def wartosc_ciagu(self, liczba):
        return self.a_1 + (liczba - 1) * self.r

    def pobierz_parametry(self):
        self.a_1 = int(input("Podaj a_1: "))
        self.r = int(input("Podaj r: "))
        self.n = int(input("Podaj n: "))

    def policz_sume(self):
        return (self.a_1 + self.wartosc_ciagu(self.n)) / 2 * self.n

    def policz_elementy(self):
        for i in range(1, self.n + 1):
            print("Wartosc elementu a_" +  str(i) + ': ' + str(self.wartosc_ciagu(i)))


Ciag = CiagArytmetyczny()
print("----------------")
Ciag.pobierz_parametry()
print("----------------")
print(Ciag.pobierz_elementy())
print("----------------")
print("Suma n elementów ciągu: " + str(Ciag.policz_sume()))
print("----------------")
print(Ciag.policz_elementy())
print("----------------")
Ciag.wyswietl_dane()
print("\n\n")

#ZADANIE 6
class Slowa:
    def __init__(self, slowo_1, slowo_2):
        self.slowo_1 = slowo_1
        self.slowo_2 = slowo_2

    def sprawdz_czy_palindrom(self):
        slowo_rev = reversed(self.slowo_1)
        if list(slowo_rev) == list(self.slowo_1):
            print(self.slowo_1 + " to słowo to palindrom")
        else:
            print("Podane słowo nie jest palindromem")

    def sprawdz_czy_metagram(self):
        other_letter = 0
        if len(self.slowo_1) == len(self.slowo_2):
            for x in range(len(self.slowo_1)):
                if list(self.slowo_1)[x] != list(self.slowo_2)[x]:
                    other_letter += 1
                    if other_letter > 1:
                        print("Podane słowa nie są metagramami")
                        break
            else:
                print("Podane słowa są metagramami")
        if other_letter == 0:
            print("Podane słowa nie są metagramami")

    def sprawdz_czy_anagram(self):
        if set(self.slowo_1) == set(self.slowo_2):
            print("Podane słowa są anagramami")
        else:
            print("Podane słowa nie są anagramami")

slowo = Slowa("alla", "alha")
slowo.sprawdz_czy_palindrom()
slowo.sprawdz_czy_metagram()
slowo.sprawdz_czy_anagram()

# ZADANIE 7
class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def __del__(self):
        print("Nie ma, usunięto")

    def idz_w_gore(self, ile_krokow):
        self.y += self.krok * ile_krokow

    def idz_w_dol(self, ile_krokow):
        self.y -= self.krok * ile_krokow

    def idz_w_lewo(self, ile_krokow):
        self.x -= self.krok * ile_krokow

    def idz_w_prawo(self, ile_krokow):
        self.x += self.krok * ile_krokow

    def podaz_gdzie_jestes(self):
        print("X: "+ str(self.x) + " Y: " + str(self.y))

Robak = Robaczek(0, 0, 2)
Robak.idz_w_gore(10)
Robak.idz_w_dol(5)
Robak.idz_w_lewo(5)
Robak.idz_w_prawo(10)
Robak.podaz_gdzie_jestes()
del Robak
# ZADANIE 1
lista = [x for x in range(101) if x % 4 == 0]
plik = open("zadanie_4_1.txt", "w")
plik.writelines(str(lista))
plik.close()

# ZADANIE 2
with open("zadanie_4_1.txt", "r") as plik:
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
maslo.wyświetl_produkt()
maslo.ile_produktu()
maslo.ile_kosztuje()
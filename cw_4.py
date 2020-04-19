#cwiczenie 4 Kacper Walczak
#zad4
class NaZakupy:
    def __init__(self, nazwa, ilosc, jednostka, cena):
        self.nazwa=nazwa
        self.ilosc=ilosc
        self.jednostka=jednostka
        self.cena=cena
    def wyswietl_produkty(self):
        print("Kup", self.nazwa ,"w ilosci", self.ilosc, self.jednostka, "za", self.cena, "za sztuke" )

    def ile_produtku(self):
        print(self.ilosc, self.jednostka)

    def ile_kosztuje(self):
        return self.cena*self.ilosc

jajka=NaZakupy("jajka",3,"szt",5)
jajka.wyswietl_produkty()
jajka.ile_produtku()
print(jajka.ile_kosztuje())
#zad7
class robaczek():
    def __init__(self):
        self.x=0
        self.y=0
    def idz_w_gore(self,ile_krokow):
        self.y+=ile_krokow
    def idz_w_dol(self,ile_krokow):
        self.y-=ile_krokow
    def idz_w_lewo(self,ile_krokow):
        self.x-=ile_krokow
    def idz_w_prawo(self,ile_krokow):
        self.x+=ile_krokow
    def pokaz_gdzie_jestes(self):
        print("Twoja pozycja x:", self.x, "y:", self.y)

gra=robaczek()
gra.idz_w_gore(10)
gra.idz_w_lewo(15)
gra.pokaz_gdzie_jestes()
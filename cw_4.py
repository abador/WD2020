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

# zad 6
def czynalezy(a="",b=""):
    for i in range(0,len(a)):
        if(a[i]==b):
            return True

def unikalnosc(a=""):
    wynik=""
    for i in range(0,len(a)):
        if(czynalezy(wynik,a[i])==None):
            wynik+=a[i]
    return wynik

class slowa:
    def __init__(self, slowo1,slowo2):
        self.slowo1 = slowo1
        self.slowo2=slowo2

    def palindrom(self):
        y = len(self.slowo1) - 1
        for i in range(0, len(self.slowo1), 1):
            if (self.slowo1[i] != self.slowo1[y]):
                return print("To nie jest Palindrom")
            else:
                y -= 1
        print("To jest Palindrom")

    def metagram(self):
        x=0
        if(len(self.slowo1)==len(self.slowo2)):
            for i in range(0, len(self.slowo2),1):
                if(self.slowo1[i]!=self.slowo2[i]):
                    x+=1
            if x == 1:
                print("To są metagramy")
            else:
                print("To nie sa metagramy")
        else:
            print("To nie sa metagramy")

    def anagramy(self):
        a = unikalnosc(self.slowo1)
        b = unikalnosc(self.slowo2)
        x = 0
        for i in range(0, len(a)):
            for j in range(0, len(b)):
                if (a[i] == b[j]):
                    x += 1
        if x == len(a):
            print("To jest anaram")
        else:
            print("To nie jest anagram")


xd = "mata"
xdd="tama"
a = slowa(xd,xdd)
a.palindrom()
a.metagram()
a.anagramy()

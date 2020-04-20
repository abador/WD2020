class ciag:
    def wyswietl_dane(self):
        print('a1: ' , self.a1)
        print('r: ' , self.r)
        print('n' , self.n)

    def wartosc_ciagu(self, liczba):
        return self.a1+(liczba-1)*self.r

    def pobierz_elementy(self):
        liczba = int(input("Podaj, który element ciągu chcesz obliczyć: "))
        return self.wartosc_ciagu(liczba)


    def pobierz_parametry(self):
        self.a1 = int(input("Podaj a1: "))
        self.r = int(input("Podaj r: "))
        self.n = int(input("Podaj n: "))

    def policz_sume(self):
        return (self.a1+self.wartosc_ciagu(self.n))/2*self.n

    def policz_elementy(self):
        for i in range(1, self.n+1):
            print("Wartosc elementu a", i, ': ', self.wartosc_ciagu(i))


MojCiag = ciag()
MojCiag.pobierz_parametry()
print(MojCiag.pobierz_elementy())
print(MojCiag.policz_sume())
print(MojCiag.policz_elementy())
MojCiag.wyswietl_dane()

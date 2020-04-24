from Rycerze.plik import *
from Rycerze.akcje import *
import random
#AUTOR:Kacper Walczak ISI grupa IV/5 czwartek 17:30

menu=["W","N","E"] #deklaracja opcji wyboru menu
menu2=["W","A","S","D","SG","P"] #deklaracja wyboru ruchów zapisu itp
answ1="" #odpowiedz do menu
answ2="" #opowiedz do gry
point={
    "pozx":0,
    "pozy":0
} #deklaracja pozycji
vector = {
        "W": 1,
        "S": 1,
        "A": 1,
        "D": 1
    }#deklaracja mozliwych ruchow
print("Rycerze\n"
      "Grajac w gre uzywaj tylo DRUKOWANYCH liter\n"
      "MENU\n"
      "N-Nowa Gra\n"
      "W-Wczytaj\n"
      "E-WYJSCIE")

while answ1 not in menu:
    answ1=input("Twoj wybor ->")#insrukcja bedzie sie powtarzac dopoki nie wybierzemy opcji z menu

if answ1=="N": #losowy przydział x i y z zakresu -100 do 100
    point["pozx"]=random.randint(-100,100)
    point["pozy"]=random.randint(-100,100)
    print("Twoja pozycja to - ", point)

elif answ1=="W":#wczytanie z pliku user_savegame danych o pozycjach
    point["pozx"] = savegame.load()[0]
    point["pozy"] = savegame.load()[1]
    print("Twoja pozycja to - ", point)
else:
    exit()

answ2 = input("Do poruszania sie uzywaj tylko klawiszy WSAD,\n"
              "Zapisac gre mozesz za pomoca SG, wyjsc-E,pokazac swoja aktualna pozycje-P -> ")

while (answ2 in menu2) or (answ2 is not None):
#powtarzanie sie dopoki nie zostanie program przerwany wszytskie inne opcje powoduja blad lub dzialanie
    if answ2 in vector:
        vector[answ2] += 1 #dodanie ruchow do vectora
        answ2 = input("(W,A,S,D,SG,E,P) ->")
    elif answ2 in "SG":#zapis gry
        point = funkcje.move(point, vector)
        savegame.save(point)
        answ2 = input("(W,A,S,D,SG,E,P) ->")
    elif answ2 in "P":#pokazuje aktualna pozycje
        point=funkcje.move(point,vector)
        print(point)
        answ2 = input("(W,A,S,D,SG,E,P) ->")
    elif answ2 in "E":
       exit()
    else:#gdy wpiszemy cos innego niz mozliwosci
        print("ERROR-twoj wybor nie jest opcja ")
        answ2 = input("(W,A,S,D,SG,E,P) ->")




# przygotuj funkcję ruch przyjmującą jako pierwszy argument obiekt klasy robaczek oraz listę owoców oraz userinput() zwracającą wybór użytkownika
#8. Na start aplikacji podajemy informacje o wszystkich obiektach w grze(współrzędne i inne atrybuty)
#9. Użytkownik wpisuje na klawiaturze gdzie ma poruszać się robaczek WSAD
#10. Aplikacja ma reagować na dane wejściowe od użytkownika
# po wykonaniu kazdego ruchu aplikacja ma informowac na standardowym wyjsciu o aktualnym stanie robaczka, jezeli zostanie zjedzony owoc to nalezy podac jego nazwe
#11. Działanie aplikacji kończy się jak lista owoców jest pusta lub użytkownik wpisze Q
# na koniec działania funkcji ruch otrzymujemy słownik jak w zadaniu 2 z aktualnym stanem gry: { robaczek: {x:, y:}, owoce: [ {x:,y:,jedzenie:,nazwa:}..... ]}
print("Aplikacja Robaczek")
print("Robaczek:\n    X - " + str(robaczek.x) + "\n    Y - " + str(robaczek.y) + "\n    Speed - " + str(robaczek.speed)
      + "\n    Hunger - " + str(robaczek.hunger) + "\n    Level - " + str(robaczek.level))
print("Owoce:")
[print("X - " + str(Owoc.list[x].x) + " Y - " + str(Owoc.list[x].y) + " Jedzenie - " + str(Owoc.list[x].jedzenie)
          + " Nazwa - " + str(Owoc.list[x].nazwa)) for x in range(len(Owoc.list))]
print("Możesz ruszać się WSAD:\n    W - Będziesz kierował się na północ\n    S - Udasz się na południe\n"
      + "    A - To kierunek na zachód\n    D - Kierunek wschód\n")

def ruch(robaczek, listaOwocow, userinput):
    if userinput == "W":
        robaczek.y += 1
    elif userinput == "S":
        robaczek.y -= 1
    elif userinput == "A":
        robaczek.x -= 1
    elif userinput == "D":
        robaczek.x += 1
    dictionary = dict()
    dictionary['robaczek'] = {'x': robaczek.x, 'y': robaczek.y}
    dictionary['owoce'] = [dictionary['owoce'].append({"x": x.x, "y": x.y, "jedzenie": x.jedzenie, "nazwa": x.nazwa})
                           for x in Owoc.list]
    return dictionary

while len(Owoc.list) != 0:
    kierunek = input("Podaj kierunek, w którym chcesz się udać: ")

    if kierunek == "Q":
        print("Q - Opuszczasz krainę")
        break

    dictonary = ruch(robaczek, Owoc.list, kierunek)

    for x in range(len(Owoc.list)):
        if toSamoPole(robaczek, Owoc.list[x]) is True:
            print("\nMniam, zjedzono " + str(Owoc.list[x].nazwa) + "\n")
            robaczek.zjedzOwoc(Owoc.list[x])
            break

    robaczek.sprawdz_poziom()

    print("Robaczek:\n    X - " + str(robaczek.x) + "\n    Y - " + str(robaczek.y) + "\n    Speed - " + str(
        robaczek.speed)
          + "\n    Hunger - " + str(robaczek.hunger) + "\n    Level - " + str(robaczek.level))

print(dictionary)
quit("KONIEC GRY")


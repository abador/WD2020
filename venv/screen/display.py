screen = [['. ' for _ in range(51)] for _ in range(51)] #PLANSZA 50x50



def canvas(x,y,paths): #PRZYJMUJE WSPOLRZEDNE POLOZENIA RYCERZA
    paths = paths[:-1]
    if(len(paths)>1):
        for path in paths:
            screen[50-path[1]][path[0]]="_ " #screen[y][x] POKAZUJE SCIEZKE RYCERZA
    screen[(50-y)][x]="X " #screen[y][x] POKAZUJE RYCERZA NA EKRANIE
    for el in screen:
        print()
        for dot in el:
            print(dot,end='')


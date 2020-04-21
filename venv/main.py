#JAKUB GOŚCINIAK IO GR I/2

from akcje import *
from screen import *
from plik import *
import random
import os

map = []

def addstep(x,y,i):
    if i<1:
        map.append(funkcje.move(point={"pozx": x, "pozy": y}, vector={"pozx": x, "pozy": y}))
    map.append(funkcje.move(point={"pozx":map[i][0],"pozy":map[i][1]},vector={"pozx":x,"pozy":y}))

def newgame():
    addstep(random.randint(-1,51),random.randint(-1,51),0)

def loadgame(map):
    i=0
    for step in map:
        addstep(step[0],step[1],i)
        i+=1

def game(steps):
    i=len(steps)-1
    while True:
        x=steps[i][0]
        y=steps[i][1]
        display.canvas(x,y,steps)
        movement = str(input())
        os.system("cls")
        if movement in "wasdQS":
            if movement =='S':
                print("Gra zapisana")
                savemode.save(steps)
                continue
            if movement.lower() == 'w':
                addstep(x,y+1,i)
                i+=1
                continue
            if movement.lower() =='s':
                addstep(x, y-1,i)
                i += 1
                continue
            if movement.lower() =='a':
                addstep(x-1, y,i)
                i += 1
                continue
            if movement.lower() =='d':
                addstep(x+1,y,i)
                i += 1
                continue
            if movement =='Q':
                exit()


def sterowanie():
    print("Po wpisaniu kierunku ruchu zatwierdź ENTEREM.")
    print("w -> W góre o 1")
    print("a -> W lewo o 1")
    print("s -> W dół o 1")
    print("d -> W prawo o 1")
    print("Nacisnij ENTER by wrocic do glownego menu.")
    input()

def menu():
    while True:
        os.system("cls")
        print("Nowa gra: 1")
        print("Wczytaj gre: 2")
        print("Sterowanie: 3")
        print("Wyjdz: 0")
        wybor = int(input())
        if wybor==1:
            newgame()
            game(map)
            return
        if wybor==2:
            loaded_map = savemode.load()
            if len(loaded_map) == 0:
                print("Brak zapisu")
                input()
                continue
            else:
                loadgame(loaded_map)
            game(map)
            return
        if wybor==3:
            sterowanie()
            menu()
            return
        if wybor==0:
            exit()




menu()

import csv
from os import path
from screen import *

def save(tab):
    try:
        f = open("venv\plik\save.txt","w+")
    except FileNotFoundError:
        f = open("plik\save.txt","w+")
    for el in tab:
        f.write("%s;%s\n" % (el[0],el[1]))
    f.close()


def load():

    steps= []
    try:
        path1 = "venv\plik\save.txt"
        if path.exists(path1):
            with open("venv\plik\save.txt",newline='') as f:
                lines = csv.reader(f,delimiter=';')
                for line in lines:
                    steps.append((int(line[0]),int(line[1])))
            f.close()
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        path2 = "plik\save.txt"
        if path.exists(path2):
            with open("plik\save.txt", newline='') as f:
                lines = csv.reader(f, delimiter=';')
                for line in lines:
                    steps.append((int(line[0]), int(line[1])))
            f.close()
    return steps
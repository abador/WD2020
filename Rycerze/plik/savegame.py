def save(point):
    plik=open("user_savegame.txt","w")
    x=str(point["pozx"])
    y=str(point["pozy"])
    linie=[x,"\n",y]
    plik.writelines(linie)
    plik.close()


def load():
    plik=open("user_savegame.txt","r")
    x=int(plik.readline())
    y=int(plik.readline())
    tab=[x,y]
    plik.close()
    return tab



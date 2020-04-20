import datetime

def save(point = {"pozx" : 0, "pozy" : 0}):
    with open("save.txt", "w+") as file:
        x = str(point["pozx"])
        file.write(str(len(x)))
        file.write(str(point["pozx"]))
        file.write(str(point["pozy"]))
        file.write("\n")
        file.write(str(datetime.datetime.now()))

def load():
    with open("save.txt", "r") as file:
        size = file.read(1)
        a = file.read(int(size))
        b = file.readline()
        print(u"\nOstatnio grałeś " + str(file.read(10)) + " o" + str(file.read(6)) + ", dobrze Cię znów widzieć")
        return [str(a), str(b)]
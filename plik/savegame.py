def save(dic, *args):
    if len(args) >= 1:
        nazwa = args[0]
        file = open(nazwa + ".txt", "w")
        file.write(dic)
        file.close()
    else:
        file = open("save.txt", "w")
        file.write(dic)
        file.close()

def load(name):
    name = str(name)
    file = open(name+".txt", "r")
    element = file.readline()
    file.close()
    return element
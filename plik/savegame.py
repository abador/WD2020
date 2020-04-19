def save(path, point):
    file = open(path, "w+")
    file.write(str(point["x"]))
    file.write("\n")
    file.write(str(point["y"]))
def load(path, point):
    file = open(path, 'r')
    point["x"] = int(file.readline())
    point["y"] = int(file.readline())
def move(point,vector):
    point["pozx"] += int(vector["W"])-int(vector["S"])
    point["pozy"] += int(vector["D"]) - int(vector["A"])
    return point
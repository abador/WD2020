def move(point,vector):
    radius = range(0,51) # UZALEZNIONE OD ROZMIARU EKRANU 50x50
    if vector["pozx"] not in radius or vector["pozy"] not in radius:
        return (point["pozx"],point["pozy"])
    else:
        point = vector
        return (point["pozx"],point["pozy"])
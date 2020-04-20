def move(point, vector):
    if int(point["pozx"]) + vector["pozx"] >=  0 and int(point["pozy"]) + vector["pozy"] >=  0:
        vector["pozx"] += int(point["pozx"])
        vector["pozy"] += int(point["pozy"])
        point["pozx"] = vector["pozx"]
        point["pozy"] = vector["pozy"]
    if int(point["pozx"]) == 0 or int(point["pozy"]) == 0:
        kierunek = ["dół" , "lewo"]
        if point["pozx"] == 0 and point["pozy"] == 0:
            print("Nie możesz iść dalej w " + kierunek[0] + " ani w " + kierunek[1] + ", musisz pójść w inną stronę")
        elif point["pozx"] == 0:
            print("Nie możesz iść dalej w " + kierunek[1] + ", musisz pójść w inną stronę")
        else:
            print("Nie możesz iść dalej w " + kierunek[0] + ", musisz pójść w inną stronę")
    return point

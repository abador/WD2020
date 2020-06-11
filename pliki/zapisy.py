def wczytaj(plik):
    dictionary = {
        "robaczek": '',
        "owoce": []
    }
    robaczek = 1
    with open(plik, "r") as file:
        for line in file:
            line = line.replace(' ', ',')
            line = line.replace('\n', '')
            line = line.split(',')
            if robaczek == 1:
                robaczek = 0
                dictionary["robaczek"] = {
                    "x": line[0],
                    "y": line[1]
                }
            else:
                dictionary["owoce"].append({
                    "x": line[0],
                    "y": line[1],
                    "jedzenie": line[2],
                    "nazwa": line[3][::-1]
                })
            #zrobić to w python compression
    return dictionary
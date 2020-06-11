# Przygotuj  funkcję toSamoPole, która przyjmuje 2 argumenty: typu Robaczek oraz Owoc, która ma sprawdzać czy znajdują się na tym samym polu
def toSamoPole(robaczek, owoc):
    if robaczek.x == owoc.x and robaczek.y == owoc.y:
        return True
    else:
        return False
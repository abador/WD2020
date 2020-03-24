def proste(a1, a2):
    if a1 == a2:
        print('Proste są równoległe')
    elif round(a1*a2) == -1:
        print('Proste są prostopadłe')

a1 = float(input("Podaj wspolczynnik a pierwszej prostej"))
a2 = float(input("Podaj wspolczynnik a drugiej prostej"))
proste(a1, a2)
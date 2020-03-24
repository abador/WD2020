produkty = {'mąka' : "kg", "bułki" : "sztuki", "kiwi" : "sztuki", "cukierki" : "kg"}
lista = [x for (x,y) in produkty.items() if y == 'sztuki']
print(lista)
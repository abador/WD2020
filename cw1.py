from math import *
#zaokraglanie
a=0.555
print(round(a))
#stała pi
print(pi)
#funkcje trygonometryczne
print(sin(2))
#pierwiatek kwadratowy
print(sqrt(9))

a, c='Ala ma kota', 'Ala\nma\ndużego\nkota'
b="""Ala
ma
dużego
kota"""
print(a)
print(b)
print(id(b)) #drukuje adres zmiennej
print(c)

del a #usuwa zmienna
print(a)
a=8
b=4
a/=b
dzielenie=a/b
print(dzielenie)
print(a)

print(u"światło")
print(u"Zażółć gęślą jaźń")
print("światło")
print("Zażółć gęślą jaźń")

print('wynik działania jest równy a=%(zm)d' % {'zm':12.5})
a=5
b=3
z=5-3

# Tworzymy przykładową listę z danymi różnych typów
lista=["Ala", 3.14, 2, 1e30, [1,2,3]]
print('Zadeklarowana lista:\n',lista)
#dodamy element na koniec
lista.append("ostatni")
print('Lista po zmianach:\n',lista)
#dodamy element na drugim miejscu
lista.insert(1,"kot")
print('Lista po zmianach:\n',lista)
slownik ={'zm':12.5}
print(slownik)

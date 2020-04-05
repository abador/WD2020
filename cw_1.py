#Cwiczenie 1 Kacper Walczak
#zad1
from math import*
print("Zad1")
a=5
b="witam"
print(a)
print(b)
#zad2
print("Zad2")
a=2
b=4
print("dodawanie :",a+b)
print("odejmowanie :",a-b)
print("dzielenie :",a/b)
print("mnozenie :",a*b)
#zad3
print("Zad3")
print("zmienna przed ",a)
a+=b
print("zmienna po ",a)
#zad4
print("zad4")
a=2
print(pow(a,10))
print(floor(3.55))
print(ceil(4.80))
#zad5
ja="KACPER"
ja2="WALCZAK"
print(ja.capitalize(), ja2.capitalize())
#zad6
la="la la la la"
print(la.count("la"))
#zad7
x="Ala ma kure"
b=len(x)
print(x[2])
print(x[b-1])
#zad8
la="la la la la"
print(la.split())
#zad9
a=5
b=3
z=5-3
print('Wynik działania %(z1)d-%(z2)d=%(z3)d' %{'z1':a, 'z2':b, 'z3':z})
#zad10
filmy=["Avengers", "Skazani na shawshank", "Harry Potter", "Iron Man", "Nietylakni"]
filmy.sort()
print("posortowane filmy:\n", filmy)
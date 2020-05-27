import math
import string
# ZADANIE 1
a, b = 3, 5
print(a, b)
c, d = 3.22 , 4.44
print(c, d)
e, f = 'KOt', "plot"
print(e, f)
g, h = 4j + 2, 2.2 + 5j
print(g, h)

# ZADANIE 2
x = int(input("Podaj liczbe: "))
y = int(input("Podaj liczbe: "))
dodawanie = x + y
print('Suma: %(zmienna)d' %{'zmienna' : dodawanie})
odejmowanie = x - y
print('Róznica: %(zmienna)d' %{'zmienna' : odejmowanie})
mnozenie = x * y
print('Iloczyn: %(zmienna)d' %{'zmienna' : mnozenie})
dzielenie = x / y
print('Iloraz: %(zmienna)d' %{'zmienna' : dzielenie})
dzielenie_calkowite = x // y
print('Dzielenie całkowite: %(zmienna)d' %{'zmienna' : dzielenie_calkowite})
reszta = x % y
print('Reszta z dzielenia: %(zmienna)d' %{'zmienna' : reszta})
potegowanie = x ** y
print('Potęgowanie: %(zmienna)d' %{'zmienna' : potegowanie})
potegowanie = pow(x,y)
print('Potęgowanie: %(zmienna)d' %{'zmienna' : potegowanie})

# ZADANIE 3
i = int(input(u"\nPodja liczbę: "))
i += 2
print(i)
i -= 2
print(i)
i *= 2
print(i)
i /= 2
print(i)
i **= 2
print(i)
i %= 2
print(i)

# ZADANIE 4
zmienna1 = math.pow(math.log(5 + pow(math.sin(8), 2), math.e) ,1 / 6)
print(zmienna1)
zmienna2 = math.floor(3.55)
print(zmienna2)
zmienna3 = math.ceil(4.80)
print(zmienna3)

# ZADANIE 5
imie = "NIKODEM"
nazwisko = "DYZMA"
print("\n" + str.capitalize(imie) + " " + str.capitalize(nazwisko))

# ZADANIE 6
tekst = """Just a small town girl
Livin' in a lonely world
She took the midnight train goin' anywhere
Just a city boy
Born and raised in south Detroit
He took the midnight train goin' anywhere
A singer in a smoky room
A smell of wine and cheap perfume
For a smile they can share the night
It goes on and on, and on, and on
Strangers waiting
Up and down the boulevard
Their shadows searching in the night
Streetlights, people
Living just to find emotion
Hiding somewhere in the night
Working hard to get my fill
Everybody wants a thrill
Payin' anything to roll the dice
Just one more time
Some will win, some will lose
Some were born to sing the blues
Oh, the movie never ends
It goes on and on, and on, and on
Strangers waiting
Up and down the boulevard
Their shadows searching in the night
Streetlights, people
Living just to find emotion
Hiding somewhere in the night
Don't stop believin'
Hold on to the feelin'
Streetlights, people
Don't stop believin'
Hold on
Streetlights, people
Don't stop believin'
Hold on to the feelin'
Streetlights, people"""
print("\n" + str(str.count(tekst, "goin'")))

# ZADANIE 7
tab = "Streetlights"
print("\n" + tab[1] + " " + tab[len(tab) - 1])

# ZADANIE 8
print(str.split(tekst))

# ZADANIE 9
zmienna1 = "String"
zmienna2 = 2.2222
zmienna3 = 0x4f
print('%(z1)s, %(z2)d, %(z3)d' %{'z1':zmienna1, 'z2':zmienna2, 'z3':zmienna3})

# ZADANIE 10
lista = ["Powwrót do przyszłości", 'Dzień Świstaka', 'Diabeł ubiera się u Prady']
lista.sort()
print('\n' + str(lista))

# ZADANIE 11
sin = [round(math.sin(0)),
        round(math.sin(math.pi / 6), 1),
        round(math.sin(math.pi / 4), 7),
        round(math.sin(math.pi / 3), 7),
        round(math.sin(math.pi / 2))]
cos = [round(math.cos(0)),
        round(math.cos(math.pi / 6), 7),
        round(math.cos(math.pi / 4), 7),
        round(math.cos(math.pi / 3), 1),
        round(math.cos(math.pi / 2))]
tan = [round(math.tan(0)),
        round(math.tan(math.pi / 6), 7),
        round(math.tan(math.pi / 4), 1),
        round(math.tan(math.pi / 3), 7),
        "NIE ISTNIEJE"]
ctan = tan.copy()
ctan.reverse()
print(sin)
print(cos)
print(tan)
print(ctan)


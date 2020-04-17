print("\n-----cw11-----\n")

#cw1
a,b=2, 3
c='project'
d='wladek_jagiello'
e=2.6
d=3.14
print(a,b)
print(c)
print(d)
print(e)

print("\n-----cw11-----\n")

#cw2
a=4
b=6
c=4
dodawanie=a+b
odejmowanie=b-c
mnozenie=a*c
dzielenie=b/c
potega=pow(b,c)
print(dodawanie)
print(odejmowanie)
print(mnozenie)
print(dzielenie)
print(potega)

print("\n-----cw11-----\n")

#cw3
a=5
a+=3
print(a)
a-=3
print(a)
a*=4
print(a)
a/=5
print(a)
a**=5
print(a)
a%=2
print(a)

print("\n-----cw11-----\n")

#cw4
from math import *
a=pow(e,10)
print(a)
b=pow(log10(5 + pow(sin(8), 2)), 1/6)
print(b)
c=floor(3.55)
print(c)
d=ceil(4.80)
print(d)

print("\n-----cw11-----\n")

#cw5
a="DAMIAN"
b="BANACH"
print(str.capitalize(a), str.capitalize(b))

print("\n-----cw11-----\n")

#cw6
tekst="la la la la la la la"
print('"la" powtarza sie', tekst.count('la'),'razy')

print("\n-----cw11-----\n")

#cw7
tekst="Tomasz Hajto wiadomo co"
print(tekst[0])
print(tekst[-1])

print("\n-----cw11-----\n")

#cw8
tekst="la la la la la la la"
print(str.split(tekst))

print("\n-----cw11-----\n")

#cw9
string='tekst'
float=69
hexdec=hex(69)
print('string: %(zm)s' % {'zm': string})
print('float: %(zm)f' % {'zm': float})
print('szestnastkowe: %(zm)s' % {'zm': hexdec})

print("\n-----cw11-----\n")

#cw10
lista=[u'Piraci z Karaibów: Skrzynia Umarlaka', 'American Pie 1', 'Shrek', 'Madagaskar']
print(u"Lista filmów:\n",lista)
lista.sort()
print(u'Lista filmów po sortowaniu:\n',lista)

print("\n-----cw11-----\n")

#cw11
tab=[
    ['kat','0','30','45','60','90'],
    ['sin', sin(0), sin(30), sin(45), sin(60), sin(90)],
    ['cos', cos(0), cos(30), cos(45), cos(60), cos(90)],
    ['tan', tan(0), tan(30), tan(45), tan(60), tan(90)]
]
print(tab[0])
print(tab[1])
print(tab[2])
print(tab[3])

print("\n-----cw12-----\n")

#cw12
zdanie=u'Tomasz Hajto w Łodzi wiadomo co'
lista=str.split(zdanie)
print(lista)

print("\n-----cw13-----\n")

#cw13
ziomy={
    'Bogdan': ['Domino','Jachaś'],
    'Król': ['Władek', 'Jagiełło'],
    'Brudas': ['Domino','Terapeuta'],
    'Darek': ['Damian', 'Banan'],
    'Elvis': ['Mateo', 'Jackie'],
    'Lord': ['Jakub', 'Tabaluga'],
    'Mushroom': ['Martin', 'Mushroom'],
    'Odrzutowy': ['Bartoelomił', 'Sanderka'],
    'Luty': ['Mateo','Styczeń'],
    'Mały': ['Andrzeh','Wazon']
}
print(ziomy['Lord'])
print(ziomy['Darek'])
print(ziomy['Bogdan'])

print("\n-----cw14-----\n")

#cw14
smsy={
    'cb': ['ciebie'],
    'bd': ['będę'],
    'tb': ['tobie'],
    'btw': ['bay the way'],
    'imo': ['in my opinion']
}
slownik={'sms': smsy}
print(slownik['sms']['cb'])
print(slownik['sms']['tb'])
print(slownik['sms']['bd'])

print("\n-----cw15-----\n")

#cw15
rzymskie={
    'I': 1, 'II': 2, 'III': 3,
    'IV': 4, 'V': 5, 'VI': 6, 'VII': 7,
    'VIII': 8, 'IX': 9, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
}
print(rzymskie)

print("\n-----cw16-----\n")

#cw16
gry={
    'TW3WD': ['The Witcher 3: Wild Hunt'],
    'TW2AoK': ['The Witcher 2: Assasins of Kings'],
    'TW': ['The Witcher'],
    'GTAV': ['Grand Theft Auto V'],
    'GTASA': ['Grand Theft Auto: San Andreas'],\
    'EU4': ['Europa Universalis IV'],
    'NFS': ['Needforspeed']
}
print('liczba elementów słownika to:',len(gry))
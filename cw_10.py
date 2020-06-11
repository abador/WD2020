import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

# ZADANIE 1
# ZADANIE 2
x = np.linspace(1, 19, 20)
plt.axis([0, 20, 0, 1])
plt.plot(x, 1/x, 'g>:',label = 'f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) dla x [1, 20]')
plt.legend()
plt.show()

# ZADANIE 3
x = np.arange(0.0, 30.0, 0.1)
plt.plot(x, np.sin(x), 'violet', label = 'f(x) = sin(x)')
plt.plot(x, np.cos(x), 'orange', label = 'f(x) = cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji sin(x) i cos(x) dla x [0, 30]')
plt.legend()
plt.show()

# ZADANIE 4
x = np.arange(0.0, 30.0, 0.1)
plt.plot(x, 2 + np.sin(x), 'blue', label = 'sin(x)')
plt.plot(x, -np.sin(x), 'orange', label = 'sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x), sin(x)')
plt.legend(loc = 'center left')
plt.show()

# ZADANIE 5


# ZADANIE 6
df = pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv', header=0, sep=',')

# # A
# m = df.groupby(["Płeć"]).agg({"Liczba":["sum"]})
# milan = m["Liczba"]["sum"]
# fig, ax = plt.subplots()
# index = np.arange(2)
# bar_width = 0.75
# ax.bar(index, milan, bar_width, color='lightblue')
# ax.set_xlabel('Lata')
# ax.set_ylabel('Liczba narodzin')
# ax.set_title("Liczba narodzin dzieci w lata 2000-2019 z podziałem zewzględu na płeć")
# ax.set_xticks(index)
# ax.set_xticklabels(("Kobiety", "Mężczyźni"), rotation = 45)
# plt.show()

# # B
# # WERSJA ALTERNATYWNA
# m = df.groupby(["Płeć", "Rok"]).agg({"Liczba": ["sum"]})
# milan = m["Liczba"]["sum"]["K"]
# inter = m["Liczba"]["sum"]["M"]
# fig, ax = plt.subplots()
# index = np.arange(20)
# bar_width = 0.3
# ax.bar(index, milan, bar_width, color='pink', label='Kobiety')
# ax.bar(index + bar_width, inter, bar_width, color='lightblue', label='Mężczyźni')
# ax.set_xlabel('Lata')
# ax.set_ylabel('Liczba narodzin')
# ax.set_title("Roczna liczba narodzin dzieci w lata 2000-2019 z podziałem ze względu na płeć")
# ax.set_xticks(index + bar_width / 2)
# ax.set_xticklabels(("2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
#                     "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"), rotation = 45)
# ax.legend()
# plt.show()
#
# # B
# m = df.groupby(["Płeć", "Rok"]).agg({"Liczba": ["sum"]})
# x = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
#      "2014", "2015", "2016", "2017", "2018", "2019"]
# y = np.arange(2000, 2020, 1)
# milan = m["Liczba"]["sum"]["K"]
# inter = m["Liczba"]["sum"]["M"]
# plt.plot(x, milan[y], 'pink', label='Kobiety')
# plt.plot(x, inter[y], 'lightblue', label='Mężczyźni')
# plt.xlabel("Lata")
# plt.ylabel('Liczba narodzin')
# plt.xticks(rotation=45)
# plt.title('Roczna liczba narodzin dzieci w lata 2000-2019 z podziałem ze względu na płeć')
# plt.legend()
# plt.show()

# # C
# m = df.groupby(["Rok"]).agg({"Liczba": ["sum"]})
# milan = m["Liczba"]["sum"]
# fig, ax = plt.subplots()
# index = np.arange(20)
# bar_width = 0.3
# ax.bar(index, milan, bar_width, color='lightblue')
# ax.set_xlabel('Lata')
# ax.set_ylabel('Liczba narodzin')
# ax.set_title("Roczna liczba narodzin dzieci w lata 2000-2019")
# ax.set_xticks(index)
# ax.set_xticklabels(("2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
#                     "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"), rotation = 45)
# plt.show()

# A
plt.subplot(1, 3, 1)
m = df.groupby(["Płeć"]).agg({"Liczba":["sum"]})
plt.bar(["Kobieta", "Mężczyna"], m["Liczba"]["sum"], color = 'darkgreen')
plt.ylabel('Liczba narodzin')
plt.xlabel("Płeć")

# B
plt.subplot(1, 3, 2)
m = df.groupby(["Płeć", "Rok"]).agg({"Liczba": ["sum"]})
x = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
     "2014", "2015", "2016", "2017", "2018", "2019"]
y = np.arange(2000, 2020, 1)
milan = m["Liczba"]["sum"]["K"]
inter = m["Liczba"]["sum"]["M"]
plt.plot(x, milan[y], 'pink', label='Kobiety')
plt.plot(x, inter[y], 'lightblue', label='Mężczyźni')
plt.xticks(rotation=45)
plt.xlabel("Lata")
plt.ylabel('Liczba narodzin')
plt.legend()

# C
plt.subplot(1, 3, 3)
m = df.groupby(["Rok"]).agg({"Liczba": ["sum"]})
x = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
     "2014", "2015", "2016", "2017", "2018", "2019"]
plt.bar(x, m["Liczba"]["sum"], color = 'darkorange')
plt.xticks(rotation=45)
plt.xlabel("Lata")
plt.ylabel('Liczba narodzin')
plt.show()

# ZADANIE 7
df = pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv', header=0, sep=',')
m = df.groupby(["Płeć", "Rok"]).agg({"Liczba": ["sum"]})
x = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
     "2014", "2015", "2016", "2017", "2018", "2019"]
y = np.arange(2000, 2020, 1)
milan = m["Liczba"]["sum"]["K"]
inter = m["Liczba"]["sum"]["M"]
plt.bar(x, milan, width=0.3, color="darkblue", label='Kobiety')
plt.bar(x, inter, width=0.3, color="darkred", label='Mężczyźni', bottom=milan)
plt.xticks(rotation=45)
plt.xlabel("Lata")
plt.ylabel('Liczba narodzin')
plt.legend(loc = 2)
plt.show()

# ZADNIE 8
def rzucaj(n):
    lista = []
    for x in range(n):
        lista.append(random.randint(1,6) + random.randint(1,6))
    return lista
n = int(input("Podaj liczbę rzutów dwiema kostkami k6: "))
x = rzucaj(n)
plt.hist(x , bins=50, facecolor='g', alpha=0.75, density=True)
plt.grid(True)
plt.xlabel("Wartości")
plt.ylabel("Prawdopodobieństwo")
plt.title("Histogram")
plt.show()

# ZADANIE 9
df = pd.read_csv('zamowienia.csv', header=0, sep=';')
m = df.groupby(["Sprzedawca"]).agg({"Utarg": ["sum"]})
df = df.groupby(["Sprzedawca"]).agg({"Sprzedawca": ["max"]})
explode = np.zeros(len(m["Utarg"]["sum"]))
explode[m["Utarg"]["sum"].argmax()] = 0.1
color = ["rosybrown", "sienna", "tan", "darkkhaki", "palegreen", "lightseagreen", "deepskyblue", "royalblue",
         "mediumpurple"]
plt.pie(m["Utarg"]["sum"], labels=df["Sprzedawca"]["max"], colors=color, startangle=170, autopct="%1.1f%%",
        explode=explode)
plt.legend(loc="best", ncol=3)
plt.title("Procentawy udział sprzedawców w obrocie firmy")
plt.show()

# ZADANIE 10
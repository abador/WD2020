import pandas as pd

# ZADANIE 1
df = pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv', header=0, sep=',')
print(df)

# ZADANIE 2
print("\nA\n" + str(df[df["Liczba"] > 1000]))

print("\nB\n" + str(df[df["Imię"] == "ŁUKASZ"]))

print("\nC\n" + str(df["Liczba"].sum()))

df2 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
print("\nD\n" + str(df2["Liczba"].sum()))

print("\nE")
print(df.groupby(["Płeć"]).agg({"Liczba":["sum"]}))

print("\nF")
m = df.groupby(["Rok","Płeć"])["Liczba"].transform("max") == df["Liczba"]
print(df[m].to_string(index=False))

print("\nG")
x = df[df["Płeć"] == "M"]
x = x.groupby(["Imię"]).agg({"Liczba":["sum"]})
x = x["Liczba"]
x = x.sort_values('sum', ascending=False)
m = x[:1]
print(m["sum"])
df = df[df["Płeć"] == "K"]
df = df.groupby(["Imię"]).agg({"Liczba":["sum"]})
df = df["Liczba"]
df = df.sort_values('sum', ascending=False)
m = df[:1]
print(m["sum"])

# ZADANIE 3
df = pd.read_csv('zamowienia.csv', header=0, sep=';')
print(df)

# A
sprzedawcy = df["Sprzedawca"]
list = sprzedawcy.unique()
print("\nA")
print(list)

# B
zamowienia_max = df.sort_values('Utarg', ascending=False)
zamowienia_max = zamowienia_max["Utarg"][:5]
print("\nB")
print(zamowienia_max.to_string(index=False))

# C
ilosc = df.set_index(["Sprzedawca", "Utarg"]).count(level="Sprzedawca")
ilosc = ilosc["idZamowienia"].to_string()
print("\nC")
print(ilosc)

# D
ilosc_kraj = df.set_index(["Kraj", "Utarg"]).count(level="Kraj")
ilosc_kraj = ilosc_kraj["idZamowienia"].to_string()
print("\nD")
print(ilosc_kraj)

# E
ilosc_pol = df[df["Kraj"] == "Polska"]
ilosc_pol = ilosc_pol[(ilosc_pol['Data zamowienia'] >= "2005-01-01") & (ilosc_pol['Data zamowienia'] <= "2005-12-31")]
ilosc_pol = ilosc_pol.set_index(["Kraj", "Utarg"]).count(level="Kraj")
ilosc_pol = ilosc_pol["idZamowienia"].to_string()
print("\nE")
print(ilosc_pol)

# F
ilosc_mean = df[(df['Data zamowienia'] >= "2004-01-01") & (df['Data zamowienia'] <= "2004-12-31")]
ilosc_mean = ilosc_mean["Utarg"]
ilosc_mean = ilosc_mean.mean()
print("\nF")
print(ilosc_mean)

# G
ilosc_2004 = df[(df['Data zamowienia'] >= "2004-01-01") & (df['Data zamowienia'] <= "2004-12-31")]
ilosc_2004.to_csv('zamówienia_2004.csv', index=False)
ilosc_2005 = df[(df['Data zamowienia'] >= "2005-01-01") & (df['Data zamowienia'] <= "2005-12-31")]
ilosc_2005.to_csv('zamówienia_2005.csv', index=False)
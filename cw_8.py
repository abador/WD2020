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

df_m = df[df["Płeć"] == "M"]
df_k = df[df["Płeć"] == "K"]
print("\nE\n" + str(df_m["Liczba"].sum()) + "\n" + str(df_k["Liczba"].sum()))

print("\nF")
for x in range(2000,2020):
    df_m = df[((df["Płeć"] == "M") & (df["Rok"] == x))]
    liczba = df_m["Liczba"].max()
    df_m = df[((df["Płeć"] == "M") & (df["Rok"] == x) & (df_m["Liczba"] == liczba))]
    df_k = df[((df["Płeć"] == "K") & (df["Rok"] == x))]
    liczba = df_k["Liczba"].max()
    df_k = df[((df["Płeć"] == "K") & (df["Rok"] == x) & (df_k["Liczba"] == liczba))]
    print(str(x) + "     " + str(df_k["Imię"]) + "\n         " + str(df_m["Imię"]) + "\n")

# G
# w tym punkcie mam problem aby wyciągnąć te konkretne maksymalne wartości
df = df[df["Płeć"] == "M"]
max = df["Liczba"].max()
d = df.groupby(["Imię"]).agg({"Liczba":['sum']})
d = df[d["liczba"] == max]
print(d["Imię"])
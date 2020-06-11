import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# # ZADANIE 1
# x = np.linspace(-100, 100, 100)
# plt.axis([-100, 100, -2000, 2000])
# plt.plot(x, 2*x*pow(x, 0.5), 'g',label = 'f(x) = (2x^2)/√x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x) dla x [-100, 100]')
# plt.legend(loc = 2)
# plt.show()
#
# # ZADANIE 2
# x = np.arange(0., 6, 0.1)
# y = np.arange(0., 6, 0.01)
# plt.plot(x, np.cos(x), 'blue', label = 'f(x) = cos(x)')
# plt.plot(x, np.sin(x), color = "orange",linestyle='dashed', label = 'f(x) = sin(x)')
# plt.plot(y, np.cos(y+np.pi), 'go', label = 'f(x) = cos(x+pi)')
# plt.plot(x, np.sin(x+np.pi), "r-.", label = 'f(x) = sin(x+pi)')
# plt.legend(loc=4)
# plt.show()
#
# # ZADANIE 3
# x = np.zeros((5, 5))
# y1 = [1,2,3,4,5]
# y2 = [2,1,2,3,4]
# y3 = [3,2,1,2,3]
# y4 = [4,3,2,1,2]
# y5 = [5,4,3,2,1]
# x[0]= y1
# x[1] = y2
# x[2] = y3
# x[3] = y4
# x[4] = y5
# z = x.T
# x = x + z
# print(x.T)
#
# # ZADANIE 4
# x = np.arange(1,101,1)
# x = x.reshape(10,10)
# v = np.diag(x)
# v1 = []
# v2 = []
# for y in range(10):
#     if y % 2 == 0:
#         for z in range(10):
#             v1.append(x[y][z])
#     else:
#         for z in range(10):
#             v2.append(x[y][z])
# print(x)
# print(v)
# print(v1)
# print(v2)

# ZADANIE 5
df = pd.read_csv('zamowienia.csv', header=0, sep=';')
m = df["Utarg"]
print("Najwyższa wartość zamówienia:   " + str(m.max()))
print("Najniższa wartość zamówienia:   " + str(m.min()))
print("Średnia wartość zamówienia:     " + str(m.mean()))
x = df["Data zamowienia"]
t = []
t2 = []
for v in range(799):
    a = list(x[v])
    y = a[0:4]
    m = a[5:7]
    y = int(y[0] + y[1] + y[2] + y[3])
    m = int(m[0] + m[1])
    t.append(y)
    t2.append(m)
df["Rok"] = t
df["Miesiac"] = t2
df = df[df["Rok"] == 2003]
df = df.groupby(["Miesiac"]).agg({"Utarg":["mean"]})
wykres = df.plot(label='Średnia wartość utargu')
wykres.set_title("Utarg w roku 2003")
wykres.legend(loc = 2)
plt.show()
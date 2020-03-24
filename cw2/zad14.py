liczba = int(input("Podaj liczbe"))
import math
try:
    pierwiastek = math.sqrt(liczba)
    print(pierwiastek)
except ValueError:
    print('Nie mozna liczyc pierwiastka z liczby ujemnej')

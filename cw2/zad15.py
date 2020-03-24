liczba = input("Podaj liczbe: ")
try:
    int(liczba)
    print("Ok liczba")
except ValueError:
    print("To nie jest liczba")
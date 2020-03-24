liczba = int(input("Podaj liczbe: "))
s=0
while liczba>0:       #dopóki zostały jakieś cyfry
    s+=liczba%10     #dodaj ostatnią cyfrę (jedności)
    liczba//=10
print("Suma cyfr: ", s)
import sys
a = int(input("Podaj wysokosc wieży(nie więcej niż 10)"))
if(a > 10):
    print('Za dużo')
else:
    for i in range(1, a+1):
        j = 0
        while(j<i):
            sys.stdout.write("A")
            j+=1
        sys.stdout.write("\n")
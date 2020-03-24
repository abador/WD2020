import math
def okrag(x=0, a=0, y=0, b=0):
    return math.sqrt((x-a)**2 + (y-b)**2)
x = float(input('Podaj x'))
a = float(input('Podaj a'))
y = float(input('Podaj y'))
b = float(input('Podaj b'))
print('Promien wynosi: ', okrag(x, a, y, b))
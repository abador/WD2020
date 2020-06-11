# Stwórz 2 Klasy: Robaczek i Owoc dziedziczące po klasie Obiekt
# 2. Klasa obiekt ma posiadać atrybuty x i y , które są współrzędnymi obiektu
# 3. Klasa Robaczek ma posiadać atrybuty zawierające: prędkość, poziom i najedzenie
# 4. Owoc posiada parametr jedzenie o losowej wartości z przedziału 1-5
# 5. Klasa robaczek ma posiadać metody zjedzOwoc przyjmujące obiekt typu Owoc(dodanie  wartości z owocu do parametru
# najedzenie i usunięcie elementu z listy) oraz metodę sprawdź poziom, która ustawia poziom Robaczka jeżeli zje
# odpowiednią ilość owoców
import random

class Obiekt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Robaczek(Obiekt):
    def __init__(self, x, y, speed, level, hunger):
        super().__init__(x, y)
        self.speed = speed
        self.level = level
        self.hunger = hunger

    def zjedzOwoc(self, owoc):
        self.hunger = self.hunger + owoc.food
        del Owoc.list[owoc]

    def sprawdzPoziom(self):
        self.level = self.hunger // 10

class Owoc(Obiekt):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.food = random.randint(1, 5)

    Owoc.list = []

robaczek = Robaczek(int(dictionary["robaczek"]["x"]), int(dictionary["robaczek"]["y"]))
Owoc.list = [Owoc(int(dictionary['owoce'][x]['x']),
                  int(dictionary['owoce'][x]['y']),
                  int(dictionary['owoce'][x]['jedzenie']),
                  dictionary['owoce'][x]['nazwa'])
            for x in range(len(dictionary['owoce']))]
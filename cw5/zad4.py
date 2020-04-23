class Point:
    """Klasa dla punktów."""
    counter = 0                     # atrybut klasy

    def __init__(self, x=0, y=0):
        """Konstuktor punktu."""
        self.x = x
        self.y = y
        self.counter += 1
        print("init: counter ={}".format(self.counter))


asd = Point(1, 2)
asd2 = Point(1, 3)
asd.counter = 2
print(asd.counter)
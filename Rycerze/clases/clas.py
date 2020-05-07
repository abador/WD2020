class Postac:
    def __init__(self,name,moves):
        self.name=name
        self.moves=moves
    def nazwij(self):
        name=input("Podaj imie swojego rycerza")
class Templariusz(Postac):
    Postac.moves=1
class Asasyn(Postac):
    Postac.moves=3
class Elf(Postac):
    Postac.moves=2
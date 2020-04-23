class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.data):
            raise StopIteration
        self.index = self.index + 1
        if self.index % 2 == 0:
            return self.data[self.index]


obiekt = Iterator("napis")

for i in obiekt:
    print(i)
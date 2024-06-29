class EvenNumbers:

    def __init__(self, start=0, stop=1,):
        self.start = start
        self.stop = stop
        self.i = 0
        self.num = 0

    def __iter__(self):
        if self.start % 2 != 0:
            self.start = self.start + 1
        return self

    def __next__(self):
        if self.num < self.stop-1:
            self.num = self.start + 2*self.i
            self.i += 1
        else:
            raise StopIteration
        return self.num


en = EvenNumbers(10, 25)
for i in en:
    print(i)
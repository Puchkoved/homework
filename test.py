# a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#  map
import math


class Figure:
    sides_count = 0

    def __init__(self, rgb, *args):
        self.sed_sides(i for i in args)
        self.filled = None
        if self.__is_valid_color(rgb):
            self.__color = rgb
        else:
            print('Неверный формат цвета, автоматически - белый')
            self.__color = [255, 255, 255]

    def __is_valid_color(self, rgb):
        if all(i in range(0, 256) for i in rgb):
            return True
        else:
            return False

    def get_color(self):
        return self.__color

    def sed_sides(self, *args):
        sorted(args)
        if all(isinstance(i, int) for i in args) and len(args) == self.sides_count:
            if self.sides_count == 1:
                self.__sides = list(args)
            if self.sides_count == 3 and args[0]+args[1] > args[3]:
                self.__sides = list(args)
            if self.sides_count == 12: ###################
                self.__sides = list(args)
        elif len(args) == 1 and all(isinstance(i, int) for i in args):
            self.__sides = [args[0] for i in range(self.sides_count)]
        else:
            self.__sides = [1 for i in range(self.sides_count)]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *args):
        super().__init__(rgb, i for i in args)
        self.__radius = len(self) / (2 * math.pi)

    def get_square(self):
        return round(math.pow(self.__radius, 2) * math.pi, 2)


class Triangle(Figure):
    sides_count = 3


    def __init__(self, rgb, *args):
        super().__init__(rgb, i for i in args)
        self.abc = self.get_sides() + [0]
        self.h_a = 2 * self.get_square() / self.abc[0]
        self.h_b = 2 * self.get_square() / self.abc[1]
        self.h_c = 2 * self.get_square() / self.abc[2]
    def get_square(self):
        return round(math.pow(math.prod(map(lambda x: ((len(self)/2)-x), self.abc)), 0.5), 2)

circle1 = Triangle((200, 200, 100), 3,4,5)
print(len(circle1))
print(circle1.get_square())
print(circle1.abc,circle1.h_c,circle1.h_a)

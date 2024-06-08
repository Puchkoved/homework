import math


class Figure:
    sides_count = 0

    def __init__(self, rgb, *args):
        self.__sides = [1 for i in range(self.sides_count)]
        self.set_sides(*args)
        self.filled = None
        if self.__is_valid_color(rgb):
            self.__color = rgb
        else:
            print('Неверный формат цвета, автоматически - белый')
            self.__color = [255, 255, 255]

    ############color##################################
    def __is_valid_color(self, rgb):
        if all(i in range(0, 256) for i in rgb):
            return True
        else:
            return False

    def set_color(self, *rgb):
        if self.__is_valid_color(rgb):
            self.__color = rgb

    def get_color(self):
        return list(self.__color)

    ##################sides################
    def __is_valid_sides(self, *args):
        args = sorted(args)
        if self.sides_count == 1 and all(isinstance(i, int) for i in args):
            return True
        elif self.sides_count == 3 and all(isinstance(i, int) for i in args):
            if args[0] + args[1] > args[2]:
                return True
            else:
                return False
        elif self.sides_count == 12 and all(isinstance(i, int) for i in args):
            if len(set(args)) == 1:
                return True
            else:
                return False

    def set_sides(self, *args):
        if len(args) == self.sides_count:
            if self.__is_valid_sides(*args):
                self.__sides = list(args)
        elif len(args) == 1 and all(isinstance(i, int) for i in args):
            self.__sides = [args[0] for i in range(self.sides_count)]


    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *args):
        super().__init__(rgb, *args)
        self.__radius = len(self) / (2 * math.pi)

    def get_square(self):
        return round(math.pow(self.__radius, 2) * math.pi, 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, *args):
        super().__init__(rgb, *args)
        self.abc = self.get_sides() + [0]
        self.__h_a = 2 * self.get_square() / self.abc[0]
        self.__h_b = 2 * self.get_square() / self.abc[1]
        self.__h_c = 2 * self.get_square() / self.abc[2]

    def get_square(self):
        return round(math.pow(math.prod(map(lambda x: ((len(self) / 2) - x), self.abc)), 0.5), 2)


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return int(math.pow(self.get_sides()[0], 3))


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

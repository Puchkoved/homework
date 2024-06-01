class Car:
    price = 1000000

    def __str__(self):
        return f'{type(self).__name__} - цена: {self.price}, лошадиные силы: {self.horse_powers()}'

    def horse_powers(self):
        return 1000

class Nissan (Car):
    price = 2000000


    def horse_powers(self):
        return 2000


class Kia(Car):

    price = 3000000


    def horse_powers(self):
        return 3000



car1 = Nissan()
car2 = Kia()

print(car1)
print(car2)
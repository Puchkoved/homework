class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def horse_powers(self):
        return 1000


class Nisan(Vehicle, Car):
    vehicle_type = 'машина'
    price = 2000000

    def  horse_powers(self):
        return 2000


car1 = Nisan()
print(car1.vehicle_type, car1.price)

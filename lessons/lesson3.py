class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

class Car:
    def __init__(self, model, year, owner):
        self.__model = model
        self.__year = year
        if type(owner) == Person:
            self.__owner = owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def drive(self):
        print(f'Car {self.model} is driving')

    def __str__(self):
        return f'Car {self.model}, {self.year}, owner: {self.owner.name}'

    def __lt__(self, other):
        return self.year < other.year

    def __gt__(self, other):
        return self.year > other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __le__(self, other):
        return self.year <= other.year

    def __ge__(self, other):
        return self.year >= other.year


class FuelCar(Car):
    total_fuel = 0

    def __init__(self, model, year, owner, fuel_consumption):
        Car.__init__(self, model, year, owner)
        self.__fuel_consumption = fuel_consumption

    @classmethod
    def buy_fuel(cls, amount):
        cls.total_fuel += amount

    @classmethod
    def fuel_car(cls, amount):
        cls.total_fuel -= amount

    @classmethod
    def get_total_fuel(cls):
        return cls.total_fuel

    @staticmethod
    def get_fuel_type():
        return 'Petrol'

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    def drive(self):
        print(f'Fuel car {self.model} is driving with fuel consumption {self.fuel_consumption}')

    def __str__(self):
        return super().__str__() + f', fuel consumption: {self.fuel_consumption}'


class ElectricCar(Car):
    def __init__(self, model, year, owner, battery_capacity):
        Car.__init__(self, model, year, owner)
        self.__battery_capacity = battery_capacity

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    def drive(self):
        print(f'Electric car {self.model} is driving with battery capacity {self.battery_capacity}')

    def __str__(self):
        return super().__str__() + f', battery capacity: {self.battery_capacity}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, owner, fuel_consumption, battery_capacity):
        FuelCar.__init__(self, model, year, owner, fuel_consumption)
        ElectricCar.__init__(self, model, year, owner, battery_capacity)

    def drive(self):
        print(f'Hybrid car {self.model} is driving with fuel consumption {self.fuel_consumption} and battery capacity {self.battery_capacity}')

    def __str__(self):
        return super().__str__() + f', fuel consumption: {self.fuel_consumption}, battery capacity: {self.battery_capacity}'


# Создаем экземпляры для тестирования

adilet = Person('Adilet', 25)

fuel_car = FuelCar('Audi', 2020, adilet, 10)
print(fuel_car)
fuel_car.drive()

battery_car = ElectricCar('Tesla', 2018, adilet, 100)
print(battery_car)
battery_car.drive()

hybrid_car = HybridCar('BMW', 2024, adilet, 10, 100)
print(hybrid_car)
hybrid_car.drive()

print(HybridCar.mro())
print(fuel_car < hybrid_car)

print(2024 - hybrid_car.owner.age)

FuelCar.buy_fuel(100)
FuelCar.fuel_car(10)
print(FuelCar.get_total_fuel())

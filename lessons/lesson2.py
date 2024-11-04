class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    def set_age(self, age):
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError("Ты ввел не верное значение возраста ")

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def get_name(self):
        return f'Name: {self.__name}'

    def set_name(self, name):
        self.__name = name

    def info(self):
        return f'Name: {self.__name}, Age: {self.__age}, Birth year: {2024 - self.__age}'

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Dog(Animal):
    def __init__(self, name, age, commands):
        super().__init__(name, age)
        self.__command = commands

    @property
    def commands(self):
        return self.__command

    @commands.setter
    def commands(self, value):
        self.__command == value

class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super().__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

# some_animal = Animal('Isa', 3)
# some_animal.set_age(5)
# some_animal.set_name('Adilet')
# print(some_animal.info())
# print(some_animal.get_name())

cat = Cat('Tom', 5)
print(cat.info())

dog = Dog('Adilet', 8, 'sit')
dog.commands = 'Sit, run'
print(dog.commands)
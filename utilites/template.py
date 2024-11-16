class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Person: Name - {self.__name}, Age - {self.__age}'

if __name__ == '__main__':
    person = Person('Alice', 18)
    print(person)
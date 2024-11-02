class Transport:
    def __init__(self, the_model, the_year, the_color):
        # attributes
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color

class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)

class Car(Transport):

    # constructor               #parameters
    def __init__(self, the_model, the_year, the_color, penalties = 0):
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties

    def signal(self, nums_of_signals, sound):
        while nums_of_signals > 0:
            print(f'{self.model} is signalling {sound}')
            nums_of_signals -= 1

class Truck(Car):
    def __init__(self, the_model, the_year, the_color, penalties = 0, load_capacity = 0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f'You cant load more than {self.load_capacity}')
        else:
            print(f'You successfully loaded the cargo of {product_type} ({weight} kg.)')


myCar = Car('BMW X-6', 2020, 'black')
best_Car = Car(the_year=2023, the_model='Honda Fit', the_color='blue')
print(f'{best_Car.model}, {best_Car.year}, {best_Car.color}')
best_Car.change_color('red')
best_Car.signal(3,'beep')
print(f'{best_Car.model}, {best_Car.year}, {best_Car.color}')
best_plane = Plane('Pegasus', 2020, 'red')
print(f'{best_plane.model}, {best_plane.year}, {best_plane.color}')
best_plane.change_color('white')
print(f'{best_plane.model}, {best_plane.year}, {best_plane.color}')

my_truck = Truck('Volva 300', 2000, 'yellow', 500, 30000)
print(f'{my_truck.model}, {my_truck.year}, {my_truck.color}, {my_truck.penalties}, {my_truck.load_capacity}')
my_truck.load_cargo(10000, 'milk')


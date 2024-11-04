class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        print(f'Area of this figure is unknown')

    def info(self):
        return f'Figure unknown, area of this figure unknown'


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        if type(self.__side_length) == int and self.__side_length > 0:
            return f'Area of the square is {self.__side_length * 2}{Figure.unit}'
        else:
            return ValueError('Invalid type or value of input')

    def info(self):
        return f'Square side length: {self.__side_length}{Figure.unit}, area: {self.__side_length * 2}{Figure.unit}'

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        if type(self.__length) == int and type(self.__width) == int and self.__width > 0 and self.__length > 0:
            return f'Area of the rectangle is {self.__length * self.__width}{Figure.unit}'
        else:
            return ValueError('Invalid type or value of input')

    def info(self):
        return f'Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit},  area: {self.__width * self.__length}{Figure.unit}'


figures = [
    Square(5), Square(10), Rectangle(3, 4), Rectangle(6, 8), Rectangle(10, 12)
]

for figure in figures:
    print(figure.info())
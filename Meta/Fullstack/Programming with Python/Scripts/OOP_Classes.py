class Car:
    # Constructor
    def __init__(self, name, color, year):
        self.__name = name # __: private
        self.__color = color
        self.__year = year

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_year(self):
        return self.__year

    def print_info(self):
        return self.__name + ' Properties:\n' + 'Color: ' + self.__color + '\nYear: ' + str(self.__year)

car = Car('Ferrari', 'Yellow', 2024)
print(car.get_color())
print(car.get_year())
print(car.get_name() + '\n')
print(car.print_info())
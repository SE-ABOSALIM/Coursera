class Animal:
    def __init__(self, name, is_fly, is_swim):
        self.name = name
        self.is_fly = is_fly
        self.is_swim = is_swim

    def print_info(self):
        return self.name + ' ' + self.is_fly + ' ' + self.is_swim

class Bird(Animal):
    def __init__(self, age):
        super().__init__(name='Bird', is_fly=True, is_swim=False)
        self.age = age

bird = Bird(15)
print(bird.print_info())
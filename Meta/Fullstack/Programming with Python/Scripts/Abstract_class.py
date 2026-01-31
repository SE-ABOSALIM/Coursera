from abc import ABC, abstractmethod

class Living(ABC):
    def __init__(self, age, is_human):
        self.age = age
        self.is_human = is_human

    @abstractmethod
    def eat(self, food):
        pass

    @abstractmethod
    def drink(self, drink):
        pass

class Person(Living):
    def eat(self, food):
        print(f'The person is Eating {food}')

    def drink(self, drink):
        print(f'The person is Drinking {drink}')


person = Person(22, True)
p_age = person.age
p_isHuman = person.is_human
print(p_age)
print(p_isHuman)
person.eat("Apple")
person.drink("Juice")
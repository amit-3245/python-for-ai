from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


# Child Class 1
class Lion(Animal):
    def make_sound(self):
        print("Roar!")


# Child Class 2
class Cow(Animal):
    def make_sound(self):
        print("Moo!")


# Objects
lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()
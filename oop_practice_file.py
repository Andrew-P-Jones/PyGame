import pygame
import sys
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Creates an Abstract Animal class that can pass on class attributes to other classes"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod         # Must be implimented in each subclass or the object wont be valid.
    def speak(self):
        pass


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f'{self.name} is a Cat Object that inherited its attributes for the Animal superclass'

class Dog(Animal):
    """Create a Dog class that inherits from Animal"""
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f'{self.name} is {self.age} years old'
    
    def speak(self):
        """Prints 'woof' to the screen"""
        print("Woof")

    def birthday(self):
        self.age += 1
        print(f"{self.name} had a bithday!")

dog = Dog("Dog", 6)

dog.speak()
print(dog)
dog.birthday()
print(dog)

# cat = Cat("urMomsCat", 4)
# print(cat)
# cat.speak()

# class Character:
#     def __init__(self, name, x, y):
#         self.name = name
#         self.x = x
#         self.y = y

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy

#     def __str__(self):
#         return f'{self.name} is at ({self.x}, {self.y})'
    
# Character1 = Character("Player1", 0, 0)

# print(Character1)

# Character1.move(1, 1)

# print(Character1)

# Character1.move(37, 7)

# print(Character1)

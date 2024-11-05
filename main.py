import pygame
import sys

class Character:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'{self.name} is at ({self.x}, {self.y})'
    
Character1 = Character("Player1", 0, 0)

print(Character1)

Character1.move(1, 1)

print(Character1)

Character1.move(37, 7)

print(Character1)
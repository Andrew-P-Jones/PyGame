from abc import ABC, abstractmethod
from tetris_constants import *
import pygame


# Bottom bar of the screen
class BottomBar:
    def __init__(self):
        self.x = 0
        self.y = HEIGHT - TILE_SIZE
        self.width = WIDTH
        self.height = TILE_SIZE

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, (self.x, self.y, self.width, self.height))



# Super Class
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def move_side(self, dx):
        pass

    def fall(self):
            self.y += TILE_SIZE

    @abstractmethod
    def rotate(self):
        pass




class Square(Shape):
    COLOR = YELLOW

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.COLOR, (self.x, self.y, TILE_SIZE * 2, TILE_SIZE * 2))


    def move_side(self, keys):
        #check to see if the shape is at the edge of the screen
        if self.x > 0:
            if keys[pygame.K_LEFT]:
                self.x -= TILE_SIZE
        if self.x < WIDTH - TILE_SIZE:    
            if keys[pygame.K_RIGHT]:
                self.x += TILE_SIZE


    def rotate(self):
        pass
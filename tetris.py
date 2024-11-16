import pygame, sys, random, time
from tetris_constants import *
from tetris_shapes import Square

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


def draw_grid(TILE_SIZE):
    for x in range(TILE_SIZE, WIDTH, TILE_SIZE):
        pygame.draw.line(SCREEN, GRAY, (x, 0), (x, HEIGHT))

    for y in range(TILE_SIZE, HEIGHT, TILE_SIZE):
        pygame.draw.line(SCREEN, GRAY, (0, y), (WIDTH, y))
#Create the falling event
move_down_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_down_event, DOWN_SPEED)


# Create shapes
square1 = Square(6, 0)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == move_down_event:
            square1.fall()
    # Logical updates


    # Fill the SCREEN with a color
    SCREEN.fill(BLACK)

    # Draw Shapes
    square1.draw(SCREEN)   

    draw_grid(TILE_SIZE)
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()
sys.exit()
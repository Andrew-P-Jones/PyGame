import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
WIDTH = 500
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
tile_size = 25

def draw_grid(tile_size):
    for x in range(tile_size, WIDTH, tile_size):
        pygame.draw.line(SCREEN, GRAY, (x, 0), (x, HEIGHT))

    for y in range(tile_size, HEIGHT, tile_size):
        pygame.draw.line(SCREEN, GRAY, (0, y), (WIDTH, y))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logical updates


    # Fill the SCREEN with a color
    SCREEN.fill(BLACK)
    draw_grid(tile_size)
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()
sys.exit()
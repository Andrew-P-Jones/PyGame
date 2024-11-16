import pygame, sys, random, time
from tetris_constants import *
from tetris_shapes import BottomBar, Square

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
# Create an event that recognizes when a key is pressed
move_side_event = pygame.USEREVENT + 2
pygame.time.set_timer(move_side_event, SIDE_SPEED)

# Create shapes
list_of_shapes = []
bar = BottomBar()
square1 = Square(6, 0)
list_of_shapes.append(bar)
list_of_shapes.append(square1)

# Current Object to move is the last object added to the list
current_shape = list_of_shapes[-1]

# A fnuction to check if the shape is at the bottom of the screen
def check_under(current_shape):
    temp_list = list_of_shapes.copy()
    temp_list.remove(current_shape)
    # print(temp_list[0].y)
    for object in temp_list:
        print(current_shape.y + TILE_SIZE *2)
        print(object.y)
        if current_shape.y + TILE_SIZE *2 == object.y and current_shape.x == object.x:
            return False
        return True
    # if shape.y + TILE_SIZE :
    #     return True
    # return False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == move_down_event:
            if check_under(current_shape) == False:
                current_shape.fall()
        elif event.type == move_side_event:
            keys = pygame.key.get_pressed()
            current_shape.move_side(keys)
    # Logical updates


    ### DRAW ###
    # Fill the Screen with Black
    SCREEN.fill(BLACK)
    # Draw Shapes
    for shape in list_of_shapes:
        shape.draw(SCREEN)  
    # Draw the grid
    draw_grid(TILE_SIZE)
    # Update the display
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()
sys.exit()
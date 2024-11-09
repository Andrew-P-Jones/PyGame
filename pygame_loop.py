import pygame
pygame.init()

WIN_WIDTH, WIN_HEIGHT = 720, 480
PADDLE_HEIGHT, PADDLE_WIDTH = 80, 10
PADDLE_DIST_FROM_SIDE = 10
BLACK = (0,0,0)
WHITE = (255, 255, 255)
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()



class Paddle():

    COLOR = WHITE
    VEL = 3
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT ))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL



def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w]:
        left_paddle.move(up=True)
    if keys[pygame.K_s]:
        left_paddle.move(up=False)

    if keys[pygame.K_UP]:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN]:
        right_paddle.move(up=False)




left_paddle = Paddle(PADDLE_DIST_FROM_SIDE, WIN_HEIGHT//2 - PADDLE_HEIGHT//2)
right_paddle = Paddle(WIN_WIDTH - PADDLE_DIST_FROM_SIDE - PADDLE_WIDTH, WIN_HEIGHT//2 - PADDLE_HEIGHT//2)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    keys = pygame.key.get_pressed()
    handle_paddle_movement(keys, left_paddle, right_paddle)

    # Do logical updates here.
    # ...
    
    # Render the graphics here.
    win.fill(BLACK)  # Fill the display with a solid color
    left_paddle.draw(win)
    right_paddle.draw(win)
    

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
import pygame
pygame.init()

WIN_WIDTH, WIN_HEIGHT = 720, 480
PADDLE_HEIGHT, PADDLE_WIDTH = 80, 10
PADDLE_DIST_FROM_SIDE = 10
BLACK = (0,0,0)
WHITE = (255, 255, 255)
SCORE_FONT = pygame.font.SysFont("comicsans", 40)
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()



class Paddle():

    COLOR = WHITE
    VEL = 4
    
    def __init__(self, x, y):
        self.x = self.x_original = x
        self.y = self.y_original = y

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT ))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.y = self.y_original
        self.x = self.x_original

class Ball():
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = -5
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y+= self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.x_vel *= -1 
        self.y_vel = 0


def paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >=0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + PADDLE_HEIGHT + left_paddle.VEL <= WIN_HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >=0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + PADDLE_HEIGHT + right_paddle.VEL <= WIN_HEIGHT:
        right_paddle.move(up=False)


# Function that will detect which part of the paddle the ball hit
# and generate a new y velocity for the ball in the opposite direction
    # first divide the paddles up into different sections
    # the paddle hight is 80 so there can be 8 different sections of 10 px 
    # use a dictionary to create the variables and store the values of y_vel
def ball_vel_generator(ball, paddle):

    number_of_sections = 8
    sections = {}    
    angles = [-5, -3, -3, -1, 1, 3, 3, 5]

    
    for i in range(number_of_sections):
        section_top = int(paddle.y + (PADDLE_HEIGHT // number_of_sections) * (i))
        section_bottom = int(paddle.y + (PADDLE_HEIGHT // number_of_sections) * (i+1))
        section_name = f"section{i}"
        sections[section_name] = (section_top, section_bottom, i)

    for section in sections:
        temp_tuple = sections[section]
        if ball.y >= temp_tuple[0] and ball.y <= temp_tuple[1]:
            ball.y_vel = angles[(temp_tuple[2])]
            break
        



def ball_collision(ball, left_paddle, right_paddle):
    # Checking to see if the ball hits the top or bottom of the screen 
    if ball.y + ball.radius >= WIN_HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1
    
    # Checking for contact with the paddles
    # Check if it is going to the right paddle
    if ball.x_vel > 0:
        # First check if the ball is within the height of the paddle
        if ball.y <= (right_paddle.y + PADDLE_HEIGHT) and ball.y >= right_paddle.y:
            # Then if the ball is touching the paddle x position
            if ball.x + ball.radius == right_paddle.x:
                ball.x_vel *= -1
                ball_vel_generator(ball, right_paddle)


    # Check if it is going to the left paddle
    if ball.x_vel < 0:
        # First check if the ball is within the height of the paddle
        if ball.y <= (left_paddle.y + PADDLE_HEIGHT) and ball.y >= left_paddle.y:
            # Then if the ball is touching the paddle x position
            if ball.x - ball.radius == left_paddle.x + PADDLE_WIDTH:
                ball.x_vel *= -1
                ball_vel_generator(ball, left_paddle)
    
def draw_score(left_score, right_score):
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIN_WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIN_WIDTH* (3/4) - right_score_text.get_width()//2, 20))

left_paddle = Paddle(PADDLE_DIST_FROM_SIDE, WIN_HEIGHT//2 - PADDLE_HEIGHT//2)
right_paddle = Paddle(WIN_WIDTH - PADDLE_DIST_FROM_SIDE - PADDLE_WIDTH, WIN_HEIGHT//2 - PADDLE_HEIGHT//2)
ball = Ball(WIN_WIDTH//2, WIN_HEIGHT//2, 5)
left_score = 0
right_score = 0

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    keys = pygame.key.get_pressed()
    paddle_movement(keys, left_paddle, right_paddle)
    ball_collision(ball, left_paddle, right_paddle)
    ball.move()

    # Do logical updates here.
    if ball.x < 0:
        right_score += 1
        ball.reset()
        left_paddle.reset()
        right_paddle.reset()
    if ball.x > WIN_WIDTH:
        left_score += 1
        ball.reset()
        left_paddle.reset()
        right_paddle.reset()

    game_over = False
    if left_score == 5:
        game_over = True
        win_text = "Left Player Won!"
    if right_score == 5:
        game_over = True
        win_text = "Right Player Won!"

    if game_over:
        text = SCORE_FONT.render(win_text, 1, WHITE)
        win.blit(text, (WIN_WIDTH//2 - text.get_width()//2, WIN_HEIGHT//2 - text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(4000)
        ball.reset()
        left_paddle.reset()
        right_paddle.reset()
        left_score = 0
        right_score = 0
    
    # Render the graphics here.
    win.fill(BLACK)  # Fill the display with a solid color
    left_paddle.draw(win)
    right_paddle.draw(win)
    ball.draw(win)
    draw_score(left_score, right_score)
    

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
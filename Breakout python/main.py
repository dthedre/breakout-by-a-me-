import pygame 
from settings import *
# importing the paddle class from the paddle.py file 
from paddle import Paddle
# import the Ball class
from ball import Ball
# import the bricks
from bricks import Bricks
from scores import ScoreBoard






# initialize pygame 
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()

# Objects 
pad = Paddle(paddle_x, paddle_y)
ball = Ball(ball_x, ball_y, screen)
bricks = Bricks(screen, brick_width, brick_height)
score = ScoreBoard(text_x, color, screen)
score.set_high_score

running = True
while running:
    screen.fill(BG_COLOR)

    # makes paddle appear on screen
    pad.appear(screen)

    # ball move
    ball.move()

    # show bricks
    bricks.show_bricks()

    # Check if ball hits brick
    for brick in bricks.bricks:
        if brick.collidepoint(ball.x, ball.y - ball.radius) or brick.collidepoint(ball.x, ball.y + ball.radius):
            bricks.bricks.remove(brick)
            ball.bounce_y()
            # Increase score by 1
            score.score += 1

        # Check if ball falls off
        if ball.y + ball.radius >= 580:
            ball.y = pad.y - ball.radius
            pygame.time.delay(2000)
            score.trials -= 1
            ball.bounce_y

    # Check if ball hits the x-axis above 
    ball.check_for_contact_on_x()
    # Check if ball hits y-axis on the side
    ball.check_for_contact_on_y()

    # Check if ball hits paddle
    if (pad.rect.y < ball.y + ball.radius < pad.rect.y + pad.height and pad.rect.x < ball.x + ball.radius < pad.rect.x + pad.width):
        ball.bounce_y()
        ball.y = ball.y - ball.radius

    # Check for quit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Checks for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pad.move_right()

    if keys[pygame.K_a]:
        pad.move_left()




    pygame.display.flip()

    # To adjust the game frame time 
    clock.tick(60)
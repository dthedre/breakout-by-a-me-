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
score.set_high_score()

def restart_game():
    pad.reset()
    ball.reset()
    bricks.reset()
    score.reset()


running = True
while running:
    screen.fill(BG_COLOR)

        # Check for quit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_0, pygame.K_KP0):
            restart_game()



    # makes paddle appear on screen
    pad.appear(screen)

    # show bricks
    bricks.show_bricks()

    # show score
    score.show_scores()

    # decide what state the game is in 
    if score.is_game_over():
        score.game_over()
    elif len(bricks.bricks) == 0:
        score.success()
    else:
        ball.move()

    # Check if ball hits the x-axis above 
    ball.check_for_contact_on_x()
    # Check if ball hits y-axis on the side
    ball.check_for_contact_on_y()

    # Check if ball hits paddle
    if (pad.rect.y < ball.y + ball.radius < pad.rect.y + pad.height and pad.rect.x < ball.x + ball.radius < pad.rect.x + pad.width):
        ball.bounce_y()
        ball.y = ball.y - ball.radius

        # Check if ball hits brick
    for index, brick in enumerate(bricks.bricks):
        if brick.collidepoint(ball.x, ball.y - ball.radius) or brick.collidepoint(ball.x, ball.y + ball.radius):
            bricks.remove(index)
            ball.bounce_y()
            score.score += 1
            break

        # Check if ball falls off
        if ball.y + ball.radius >= 580:
            ball.y = pad.y - ball.radius
            pygame.time.delay(2000)
            score.trials -= 1
            ball.reset()

    # Check if there are more trials
    if score.game_over():
        score.game_over()
    # Check if all bricks are broken
    elif len(bricks.bricks) == 0:
        score.success()
    else:
        ball.move()


    # Checks for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pad.move_right()

    if keys[pygame.K_a]:
        pad.move_left()




    pygame.display.flip()

    # To adjust the game frame time 
    clock.tick(60)
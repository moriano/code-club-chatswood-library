import pygame

from sprites import Ball
from sprites import Paddle
from constants import GAME_SCREEN_WIDTH, CAME_SCREEN_HEIGHT
from constants import WHITE, BLACK

pygame.init()

size = (GAME_SCREEN_WIDTH, CAME_SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

left_paddle = Paddle(WHITE, 10, 120)
left_paddle.rect.x = 50
left_paddle.rect.y = 200

right_paddle = Paddle(WHITE, 10, 120)
right_paddle.rect.x = GAME_SCREEN_WIDTH - 50
right_paddle.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = GAME_SCREEN_WIDTH / 2
ball.rect.y = CAME_SCREEN_HEIGHT / 2

#  This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(left_paddle)
all_sprites_list.add(right_paddle)
all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carry_on = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carry_on:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carry_on = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carry_on = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.move_up(10)
    if keys[pygame.K_s]:
        left_paddle.move_down(10)
    if keys[pygame.K_UP]:
        right_paddle.move_up(10)
    if keys[pygame.K_DOWN]:
        right_paddle.move_down(10)

    # --- Game logic should go here
    all_sprites_list.update()

    #  Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= GAME_SCREEN_WIDTH or ball.rect.x <= 0:
        ball.x_movement = -ball.x_movement
    if ball.rect.y > CAME_SCREEN_HEIGHT or ball.rect.y < 0:
        ball.y_movement = -ball.y_movement

    #  Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, left_paddle) or pygame.sprite.collide_mask(ball, right_paddle):
        ball.bounce()

    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLACK)
    #  Draw the net
    pygame.draw.line(screen, WHITE, [GAME_SCREEN_WIDTH/2, 0], [GAME_SCREEN_WIDTH/2, CAME_SCREEN_HEIGHT], 5)

    #  Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
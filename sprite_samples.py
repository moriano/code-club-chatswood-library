import pygame
from random import randint
pygame.init()


class Hero(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(16, 16, 16, 16)
        self.image = pygame.Surface([16, 16])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, WHITE, [0, 0, 16, 16])

    def moveUp(self):
        self.rect.y -= 5

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

all_sprites_list = pygame.sprite.Group()

hero = Hero()

all_sprites_list.add(hero)

hero.rect.x = 20
hero.rect.y = 200

all_sprites_list.add(hero)

clock = pygame.time.Clock()

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

keepGoing = True
while keepGoing:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            keepGoing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x: #Pressing the x Key will quit the game
                keepGoing = False

    # Capture user input
    all_sprites_list.update()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hero.moveUp()



    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
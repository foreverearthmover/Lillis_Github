# importing required library
import pygame
import random
import math

# constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0,0,0)

# activate the pygame library
pygame.init()

# display surface object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the pygame window name
pygame.display.set_caption('awkward cats in space')

class Cat:
    def __init__(self):
        self.pos_x = 100
        self.pos_y = 100
        img = pygame.image.load("cat.png")
        self.original_img = pygame.transform.scale(img, (150, 150))
        self.img = self.original_img.copy()

        # random initialization for position and speed
        self.center_x = random.randint(100, SCREEN_WIDTH - 200)
        self.center_y = random.randint(100, SCREEN_HEIGHT - 200)
        self.radius = random.randint(50, 150)
        self.angle = random.uniform(0, 2 * math.pi)
        self.rotation_angle = 0
        self.speed = random.uniform(0.03, 0.03)

        # random color tint
        self.tint_color = (
            random.randint(0, 50),
            random.randint(0, 50),
            random.randint(0, 50)
        )
        self.tint()

        # position calculation
        self.animate()

    def flip(self):
        self.original_img = pygame.transform.flip(self.original_img, True, random.choice([True, False]))

    def tint(self):
        self.original_img.fill((*self.tint_color, 100), special_flags=pygame.BLEND_ADD)

    def animate(self):
        # circle
        self.pos_x = self.center_x + self.radius * math.cos(self.angle)
        self.pos_y = self.center_y + self.radius * math.sin(self.angle)

        # rotate image
        self.rotation_angle = (self.rotation_angle + 1) % 360
        self.img = pygame.transform.rotate(self.original_img, self.rotation_angle)

        # update angle for circular motion
        self.angle += self.speed

    def draw(self):
        screen.blit(self.img, (self.pos_x, self.pos_y))

# create objects
cats = [Cat() for _ in range(random.randint(3, 10))]

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    # paint the screen with background color
    screen.fill(BACKGROUND_COLOR)

    # update img position
    for cat in cats:
        cat.animate()
        cat.draw()

    # refresh the display
    pygame.display.flip()

    # code you need to end pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()
exit(0)
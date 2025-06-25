import pygame
from pygame import mixer
import sys

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
POS_X, POS_Y = 0, 0
# size and pos of clickable area
BUTTON_WIDTH = 310
BUTTON_HEIGHT = 203
BUTTON_X = 135
BUTTON_Y = 190

pygame.init()
mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Late Night Shenanigans")

# load images and music
background_img = pygame.image.load("media/bg_img.png").convert()
button_img = pygame.image.load("media/button.png").convert_alpha()
alt_img1 = pygame.image.load("media/img1.png").convert_alpha()
alt_img2 = pygame.image.load("media/img2.png").convert_alpha()
alt_img3 = pygame.image.load("media/img3.png").convert_alpha()

mixer.music.load("media/error.mp3")
mixer.music.set_volume(0.7)

button_rect = pygame.Rect(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

# font for text
font = pygame.font.Font(None, 25)

# initial instruction message
INSTRUCTION_MESSAGE = "It's late but you still want to watch some videos, click on the screen to continue."

# messages to display for each click
CLICK_MESSAGES = [
    "Oh.. a message. \"Did you submit that essay alr?\" OH NO",
    "I thought I had time until tomorrow!! Who sets a deadline to 6 am anyway??",
    "Wow."
]

current_image = button_img
click_count = 0
current_message = INSTRUCTION_MESSAGE
first_click = False

running = True
while running:
    screen.blit(background_img, (0, 0))

    # Check if mouse is hovering over rect
    mouse_pos = pygame.mouse.get_pos()
    is_hovering = button_rect.collidepoint(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not first_click:
                first_click = True
                current_message = ""  # clear the instruction message
            elif button_rect.collidepoint(event.pos):
                click_count += 1
                # cycle through images
                if click_count == 1:
                    current_image = alt_img1
                    current_message = CLICK_MESSAGES[0]
                elif click_count == 2:
                    current_image = alt_img2
                    current_message = CLICK_MESSAGES[1]
                elif click_count == 3:
                    mixer.music.play()
                    current_image = alt_img3
                    current_message = CLICK_MESSAGES[2]

    screen.blit(current_image, (0, 0))

    if is_hovering:
        hover_rect = button_rect.inflate(10, 10)
        pygame.draw.rect(screen, (255, 255, 255), hover_rect, 2)

    # draw current messages in top right
    if current_message:
        text_surface = font.render(current_message, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        screen.blit(text_surface, (SCREEN_WIDTH - text_rect.width - 50, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()
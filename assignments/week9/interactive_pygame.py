import pygame
import random
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Vampire Hunt')
clock = pygame.time.Clock()


class Character:
    def __init__(self, x, y, size, color):
        self._x = x
        self._y = y
        self._size = size
        self._color = color
        self._speed = 5

    def get_position(self):
        return (self._x, self._y)

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        pygame.draw.circle(screen, self._color, (self._x, self._y), self._size)


class Vampire(Character):
    def __init__(self, x, y):
        super().__init__(x, y, 20, RED)
        self._health = 100
        self._score = 0

    def move(self, keys):
        if keys[pygame.K_LEFT] and self._x > self._size:
            self._x -= self._speed
        if keys[pygame.K_RIGHT] and self._x < SCREEN_WIDTH - self._size:
            self._x += self._speed
        if keys[pygame.K_UP] and self._y > self._size:
            self._y -= self._speed
        if keys[pygame.K_DOWN] and self._y < SCREEN_HEIGHT - self._size:
            self._y += self._speed

    def get_score(self):
        return self._score

    def increment_score(self):
        self._score += 1


class Prey(Character):
    def __init__(self):
        x = random.randint(20, SCREEN_WIDTH - 20)
        y = random.randint(20, SCREEN_HEIGHT - 20)
        super().__init__(x, y, 10, WHITE)


def show_start_screen():
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font('Bleeding_Cowboys.ttf', 44)
    title = font.render('Vampire Night Hunt', True, WHITE)
    font = pygame.font.SysFont('Arial', 32)
    instructions = font.render('Use arrow keys to move. Catch the prey to score!', True, WHITE)
    start = font.render('Click anywhere to start', True, WHITE)

    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
    screen.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, 300))
    screen.blit(start, (SCREEN_WIDTH // 2 - start.get_width() // 2, 350))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


def main():
    show_start_screen()

    vampire = Vampire(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    prey = Prey()

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        vampire.move(keys)

        # Check collision
        vampire_pos = vampire.get_position()
        prey_pos = prey.get_position()
        distance = math.sqrt((vampire_pos[0] - prey_pos[0]) ** 2 + (vampire_pos[1] - prey_pos[1]) ** 2)

        if distance < vampire._size + prey._size:
            vampire.increment_score()
            prey = Prey()

        # Draw
        screen.fill(BACKGROUND_COLOR)
        vampire.draw()
        prey.draw()

        # Display score
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f'Score: {vampire.get_score()}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()


#Game Instructions:
#- Use arrow keys to move the vampire (red circle)
#- Catch the prey (white circles) to score points
#- Close the window to exit


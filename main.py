import pygame

from game import Game
from mario import Mario

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = "#004400"


class Circle:
    def __init__(self):
        self.x_pos = 0
        self.v = 3  # пикселей в секунду

    def render(self, screen):
        self.x_pos += self.v
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x_pos), 200), 20)


def main():
    pygame.init()
    pygame.display.set_caption('Mario')
    screen = pygame.display.set_mode(WINDOW_SIZE)

    circle = Circle()
    mario = Mario(100, 100)
    game = Game(circle, mario)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BACKGROUND_COLOR)
        game.render(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()

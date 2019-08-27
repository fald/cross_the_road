import pygame
from pygame.locals import *
from settings import *

class App:
    def __init__(self):
        print(pygame.version)

        pygame.init()
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.game_screen.fill(COLOR_MAIN)
        pygame.display.set_caption(SCREEN_CAPTION)
        self.run_game()

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        quit() # Hmm.
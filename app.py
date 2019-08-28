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

        self.images = self.load_images()
        self.game_screen.fill(COLOR_MAIN)
        pygame.display.set_caption(SCREEN_CAPTION)
        self.run_game()

    def load_images(self):
        folder = "./assets/"
        files = ["background", "enemy", "player", "treasure"]
        images = {}
        for f in files:
            images[f] = pygame.transform.scale(pygame.image.load(folder + f + ".png"), (50, 50)) # Scaled but bad resolution.

        return images

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.game_screen.blit(self.images['player'], (0, 0))

            pygame.display.update()
            self.clock.tick(FPS)

            # pygame.draw.rect(self.game_screen, COLOR_WHITE, [400, 100, 100, 100])
            # pygame.draw.circle(self.game_screen, COLOR_BLACK, (450, 150), 50)

        pygame.quit()
        quit() # Hmm.
import pygame
from pygame.locals import *
from settings import *
from player import Player

class App:
    def __init__(self):
        print(pygame.version)

        pygame.init()
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # self.images = self.load_images()
        pygame.display.set_caption(SCREEN_CAPTION)
        self.run_game()

    # Unused.
    def load_images(self):
        folder = "./assets/"
        files = ["background", "enemy", "player", "treasure"]
        images = {}
        for f in files:
            images[f] = pygame.transform.scale(pygame.image.load(folder + f + ".png"), (50, 50)) # Scaled but bad resolution.

        return images

    def load_entities(self):
        pass

    def run_game(self):
        player = Player("Player", 0, 0, "./assets/player.png", 50, 50)
        direction = (0, 0)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Can definitely do prettier control handling.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        direction = (1, 0)
                    elif event.key == pygame.K_LEFT:
                        direction = (-1, 0)
                elif event.type == pygame.KEYUP:
                    if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                        direction = (0, 0)
            

            # self.game_screen.blit(self.images['player'], (0, 0))
            player.move(direction)
            
            self.game_screen.fill(COLOR_MAIN)
            self.game_screen.blit(player.image, player.location)

            pygame.display.update()
            self.clock.tick(FPS)

            # pygame.draw.rect(self.game_screen, COLOR_WHITE, [400, 100, 100, 100])
            # pygame.draw.circle(self.game_screen, COLOR_BLACK, (450, 150), 50)

        pygame.quit()
        quit() # Hmm.
import pygame
from pygame.locals import *
from settings import *
from player import Player
from npc import NPC
from entity import Entity
from random import randint

class App:
    def __init__(self):
        print(pygame.version)

        pygame.init()
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.fonts = [
            pygame.font.SysFont("Comic Sans", 79),
            pygame.font.SysFont("Comic Sans", 75)
        ]
        self.cur_wins = 0
        self.background = pygame.transform.scale(
            pygame.transform.rotate(pygame.image.load("./assets/background.png"), 270), (SCREEN_WIDTH, SCREEN_HEIGHT))

        # self.images = self.load_images()
        pygame.display.set_caption(SCREEN_CAPTION)
        self.run_game()

    def win_game(self, text):
        self.cur_wins += 1
        for t in text:
            self.game_screen.blit(t, ((SCREEN_WIDTH - t.get_width()) / 2, (SCREEN_HEIGHT - t.get_height()) / 2))
        pygame.display.update()
        self.clock.tick(1)

    def lose_game(self, text):
        self.cur_wins = 0
        for t in text:
            self.game_screen.blit(t, ((SCREEN_WIDTH - t.get_width()) / 2, (SCREEN_HEIGHT - t.get_height()) / 2))
        pygame.display.update()
        self.clock.tick(1)

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

    def render_text(self, text, antialias=True):
        t1 = self.fonts[0].render(text, antialias, COLOR_BLACK)
        t2 = self.fonts[1].render(text, antialias, COLOR_WHITE)
        return t1, t2

    def run_game(self):
        player = Player("Player", 20, SCREEN_HEIGHT / 2 - 25, "./assets/player.png", 50, 50)
        direction = (0, 0)

        max_mob_speed = self.cur_wins ** 2 + 10
        num_enemies = int(1 + self.cur_wins / 5)
        enemies = []
        for i in range(num_enemies):
            # first_x = 20 * 2 + 50
            # last_x = SCREEN_WIDTH - first_x - 50
            x_pos = int(((SCREEN_WIDTH - 20 * 2 - 50 * 2) / (num_enemies + 1)) * (i + 1))
            y_pos = randint(20, SCREEN_HEIGHT - 20 - 50)
            mob_speed = randint(10 + self.cur_wins, max_mob_speed)
            enemies.append(NPC("Squiggles"+str(i), x_pos, y_pos, "./assets/enemy.png", 50, 50, start_speed=mob_speed))
        treasure = Entity("Treasure", SCREEN_WIDTH - 20 - 50, SCREEN_HEIGHT / 2 - 25, "./assets/treasure.png", 50, 50)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Can definitely do prettier control handling.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        break
                    # wow 2 whole directions, golly gee.
                    elif event.key == pygame.K_RIGHT:
                        direction = (1, 0)
                    elif event.key == pygame.K_LEFT:
                        direction = (-1, 0)
                elif event.type == pygame.KEYUP:
                    if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                        direction = (0, 0)
            

            # self.game_screen.blit(self.images['player'], (0, 0))
            player.move(direction, self.game_screen)
            for mob in enemies:
                mob.move(self.game_screen)

            for mob in enemies:
                if player.collide(mob):
                    text = self.render_text("You suck.")
                    self.lose_game(text)
                    self.run_game()
            if player.collide(treasure):
                text = self.render_text("There is only harshness ahead.")
                self.win_game(text)
                self.run_game()

            # self.game_screen.fill(COLOR_MAIN)
            self.game_screen.blit(self.background, (0, 0))
            player.draw(self.game_screen)
            # Is this significantly less efficient than having the one loop handle collision + drawing?
            # I guess in complex stuff its not even feasible to do together, but doesn't that increase inefficiency? Pah.
            for mob in enemies:
                mob.draw(self.game_screen)
            treasure.draw(self.game_screen)

            pygame.display.update()
            self.clock.tick(FPS)

            # pygame.draw.rect(self.game_screen, COLOR_WHITE, [400, 100, 100, 100])
            # pygame.draw.circle(self.game_screen, COLOR_BLACK, (450, 150), 50)

        pygame.quit()
        quit() # Hmm.
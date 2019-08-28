import pygame

class Entity:
    def __init__(self, name, x, y, image, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.name = name

    @property
    def location(self):
        return self.x, self.y

    def draw(self, background):
        background.blit(self.image, self.location)

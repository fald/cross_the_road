from entity import Entity

class NPC(Entity):
    def __init__(self, name, x, y, image, width, height, start_speed=10):
        super().__init__(name, x, y, image, width, height)
        self.speed = start_speed

    def move(self, game_screen):
        # Ughhhhh. 2-d movement, awful implementation, TODO: start here when you come back tho this project.
        if (self.y <= 20): # Top side of screen + buffer
            self.speed = abs(self.speed)
        elif (self.y >= (game_screen.get_height() - 20 - self.height)):
            self.speed = -abs(self.speed)

        self.y += self.speed

        
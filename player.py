from entity import Entity

class Player(Entity):

    SPEED = 10 # Or in __init__?

    def __init__(self, name, x, y, image, width, height):
        super().__init__(name, x, y, image, width, height)

    def move(self, dir):
        # Robust or nah?
        self.x += dir[0] * Player.SPEED
        self.y += dir[1] * Player.SPEED
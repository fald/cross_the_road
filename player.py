from entity import Entity

class Player(Entity):

    SPEED = 10 # Or in __init__?

    def __init__(self, name, x, y, image, width, height):
        super().__init__(name, x, y, image, width, height)

    def move(self, dir, screen):
        # Robust or nah?
        # Oh god the bounds checking
        # Super great; TODO: Fix this shit-show
        s_w = screen.get_width()
        if ((dir[0] > 0 and self.x < s_w - self.width) or (dir[0] < 0 and self.x > 0)):
            self.x += dir[0] * Player.SPEED
        if (self.y in range(-Player.SPEED, screen.get_height() - self.height)):
            self.y += dir[1] * Player.SPEED

    def collide(self, other):
        if (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        ):
            return True
        return False

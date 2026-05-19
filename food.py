import random 
import settings
class Food:
    def __init__(self):
        self.position = self.spawn()
    def spawn(self):
        x=random.randrange(0, settings.WIDTH, settings.BLOCK_SIZE)
        y=random.randrange(0, settings.HEIGHT, settings.BLOCK_SIZE)
        return [x,y]
    def respawn(self):
        self.position = self.spawn()
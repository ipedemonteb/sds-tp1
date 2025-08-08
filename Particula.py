import math

class Particula:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def dist(self, particula):
        return math.sqrt((self.x - particula.x)**2 + (self.y - particula.y)**2)

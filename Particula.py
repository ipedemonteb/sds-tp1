import math

class Particula:
    def __init__(self,x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def set_ind(self, ind):
        self.ind = ind

    def dist(self, particula):
        d = math.sqrt((self.x - particula.x)**2 + (self.y - particula.y)**2)
        return 0 if d == 0 else d - self.r - particula.r
    
    def __eq__(self, other):
        return isinstance(other, Particula) and self.ind == other.ind
    
    def __str__(self):
        return f"x = {self.x}, y = {self.y}, r = {self.r}"

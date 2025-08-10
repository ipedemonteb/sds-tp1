import math

class Particula:
    def __init__(self,x, y, r, v_x, v_y):
        self.x = x
        self.y = y
        self.r = r
        self.v_x = v_x
        self.v_y = v_y
    
    def set_ind(self, ind):
        self.ind = ind

    def dist(self, particula):
        d = math.sqrt((self.x - particula.x)**2 + (self.y - particula.y)**2)
        return 0 if d == 0 else d - self.r - particula.r
    
    def dist_with_periodic_condition(self, particula, L):
        dx = self.x - particula.x
        dy = self.y - particula.y
        dx -= L * round(dx / L)
        dy -= L * round(dy / L)
        d = math.sqrt(dx**2 + dy**2)
        return 0 if d == 0 else d - self.r - particula.r

    def __eq__(self, other):
        return isinstance(other, Particula) and self.ind == other.ind
    
    def __str__(self):
        return f"x = {self.x}, y = {self.y}, r = {self.r}"

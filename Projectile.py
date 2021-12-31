import pygame

class Projectile(object):
    def __init__(self, x, y, radius, color, facing) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win) -> None:
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

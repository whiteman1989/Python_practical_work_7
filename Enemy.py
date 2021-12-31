import pygame

class Enemy(object):
    
    def __init__(self, x, y, width, height, end) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walk_count = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.hit_count = 0

    walk_right = [pygame.image.load('sprites/enemy/R1E.png'),
    pygame.image.load('sprites/enemy/R2E.png'),
    pygame.image.load('sprites/enemy/R3E.png'),
    pygame.image.load('sprites/enemy/R4E.png'),
    pygame.image.load('sprites/enemy/R5E.png'),
    pygame.image.load('sprites/enemy/R6E.png'),
    pygame.image.load('sprites/enemy/R7E.png'),
    pygame.image.load('sprites/enemy/R8E.png'),
    pygame.image.load('sprites/enemy/R9E.png'),
    pygame.image.load('sprites/enemy/R10E.png'),
    pygame.image.load('sprites/enemy/R11E.png')]

    walk_left = [pygame.image.load('sprites/enemy/L1E.png'),
    pygame.image.load('sprites/enemy/L2E.png'),
    pygame.image.load('sprites/enemy/L3E.png'),
    pygame.image.load('sprites/enemy/L4E.png'),
    pygame.image.load('sprites/enemy/L5E.png'),
    pygame.image.load('sprites/enemy/L6E.png'),
    pygame.image.load('sprites/enemy/L7E.png'),
    pygame.image.load('sprites/enemy/L8E.png'),
    pygame.image.load('sprites/enemy/L9E.png'),
    pygame.image.load('sprites/enemy/L10E.png'),
    pygame.image.load('sprites/enemy/L11E.png')]

    def draw(self, win) -> None:
        self.move()
        if self.walk_count + 1 >= 33:
            self.walk_count = 0
        
        if self.vel > 0:
            win.blit(self.walk_right[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        else:
            win.blit(self.walk_left[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        self.hitbox = (self.x + 15, self.y, 28, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walk_count = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walk_count = 0

    def hit(self):
        self.hit_count += 1
        print('Hit', self.hit_count)
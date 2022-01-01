import pygame
from pygame.examples.freetype_misc import run
from Projectile import Projectile
from Side import Side
from Enemy import Enemy

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("practical work 5")

walk_right = [pygame.image.load('sprites/R1E.png'),
pygame.image.load('sprites/R2E.png'),
pygame.image.load('sprites/R3E.png'),
pygame.image.load('sprites/R4E.png'),
pygame.image.load('sprites/R5E.png'),
pygame.image.load('sprites/R6E.png')]

walk_left = [pygame.image.load('sprites/L1E.png'),
pygame.image.load('sprites/L2E.png'),
pygame.image.load('sprites/L3E.png'),
pygame.image.load('sprites/L4E.png'),
pygame.image.load('sprites/L5E.png'),
pygame.image.load('sprites/L6E.png')]

bg = pygame.image.load('sprites/NBG.png')
player_stand = pygame.image.load('sprites/R7E.png')

clock = pygame.time.Clock()

x = 50
y = 525
width = 60
height = 71
speed = 5

is_jump = False
jump_count = 10

left = False
right = False
anim_count = 0
hitbox = (x+20, y, 28, 60)
last_direction = Side.RIGHT

shoot_loop = 0

goblin = Enemy(5, 436, 64, 64, 495)

def draw_window():
    global anim_count
    win.blit(bg, (0,0))
    if anim_count +1 >= 30:
        anim_count = 0
    
    if left:
        win.blit(walk_left[anim_count // 5], (x,y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // 5], (x, y))
        anim_count += 1
    else:
        win.blit(player_stand, (x,y))
    for projectile in projectiles:
        projectile.draw(win)
    goblin.draw(win)
    hitbox = (x+10, y, 28, 60)
    pygame.draw.rect(win, (255, 0, 0), hitbox, 2)

    pygame.display.update()

run = True

projectiles = []

while run:
    clock.tick(30)
    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for projectile in projectiles:
        if projectile.y - projectile.radius < goblin.hitbox[1] + goblin.hitbox[3] and projectile.y + projectile.radius > goblin.hitbox[1]:
            if projectile.x + projectile.radius > goblin.hitbox[0] and projectile.x - projectile.radius < goblin.hitbox[1] + goblin.hitbox[3]:
                goblin.hit()
                projectiles.pop(projectiles.index(projectile))

        if projectile.x < 500 and projectile.x > 0:
            projectile.x += projectile.vel
        else:
            projectiles.pop(projectiles.index(projectile))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f] and shoot_loop == 0:
        if last_direction == Side.RIGHT:
            facing = 1
        else:
            facing = -1
        if len(projectiles) < 5:
            projectiles.append(Projectile(round(x + width // 2), round(y + height // 2), 3, (255, 0, 0), facing))
        shoot_loop = 1
    if keys[pygame.K_LEFT] and x > 5:
        x-= speed
        left = True
        right =False
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x+= speed
        left = False
        right = True
    else:
        left = False
        right =False
        anim_count = 0
    if not (is_jump):
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] and y < 500 - height -5:
            y += speed
        if keys[pygame.K_SPACE]:
            is_jump = True

    else:
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count**2)/2
            else:
                y -= (jump_count**2)/2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    draw_window()
pygame.quit()
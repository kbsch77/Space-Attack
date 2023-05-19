import pygame
import random
import display as d
import constants as c

enemyImage = pygame.image.load('visuals/alien.png')
enemyX = random.randint(0, c.SCREEN_WIDTH)
enemyY = random.randint(50, 400)
enemyX_Change = 4
enemyY_Change = 32

def enemy(x,y):
    d.screen.blit(enemyImage, (x, y))
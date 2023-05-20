import pygame
import random
import math
import display as d
import constants as c

enemyImage = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
numofEnemies = 10

for i in range(numofEnemies):
    enemyImage.append(pygame.image.load('visuals/alien.png'))
    enemyX.append(random.randint(1, c.SCREEN_WIDTH - 32))
    enemyY.append(random.randint(50, 400))
    enemyX_Change.append(5)
    enemyY_Change.append(32)

explosionImage = pygame.image.load('visuals/explode.png')

def enemy(x, y, i):
    d.screen.blit(enemyImage[i], (x, y))

def explode(x,y):
    d.screen.blit(explosionImage, (x, y))

def isCollision(enemyX, enemyY, laserX, laserY):
    distance = math.sqrt((math.pow(enemyX - laserX, 2)) + (math.pow(enemyY - laserY, 2)))
    if distance < 27:
        return True
    else: 
        return False
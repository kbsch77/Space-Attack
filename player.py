import pygame
import display as d

playerImage = pygame.image.load('visuals/001-space-invaders.png')
playerX = 384
playerY = 680
playerX_Change = 0

laserImage = pygame.image.load('visuals/laser.png')
laserImage = pygame.transform.rotate(laserImage, 180)
laserX = 0
laserY = 680
laserY_Change = 20
laserState = "ready"

def player(x,y):
    d.screen.blit(playerImage, (x, y))

def fire_laser(x,y):
    global laserState
    laserState = "fire"
    d.screen.blit(laserImage, (x + 4, y - 10))
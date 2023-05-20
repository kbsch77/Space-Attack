import pygame
import display as d

# needed for font
pygame.init()

# score and points
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def showScore():
    score = font.render("Score :" + str(scoreValue), True, (255,255,255))
    d.screen.blit(score, (textX, textY))
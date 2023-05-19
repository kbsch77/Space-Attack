import pygame
import constants as c
     
# create a surface on screen that has the size of 1000 x 700
screen = pygame.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))

# game icon & caption
icon = pygame.image.load('visuals/alien-head.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Attack")

# set background image
def background():
    background = pygame.image.load('visuals/Space.jpg')
    screen.blit(background, (0, 0))
import pygame
import constants as c

pygame.display.set_caption("Space Attack")
     
# create a surface on screen that has the size of 1000 x 700
screen = pygame.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))

# set background image
background = pygame.image.load(c.BACKGROUND)
screen.blit(background, (0, 0))
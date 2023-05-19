import pygame

import constants as c
import display as d
import player as p
import enemy as e

def main():
     
    # initialize the pygame module
    pygame.init()
     
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        #sets backgrounf image
        d.background()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            # quits the game
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # player movement
                if event.key == pygame.K_a:
                    p.playerX_Change = -7
                if event.key == pygame.K_d:
                    p.playerX_Change = 7

                # fire laser
                if event.key == pygame.K_SPACE:
                    if p.laserState is "ready":
                        p.laserX = p.playerX
                        p.fire_laser(p.laserX, p.laserY)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    p.playerX_Change = 0

        # laser movement
        if (p.laserY <= 0): 
            p.laserY = p.playerY
            p.laserState = "ready"
        if (p.laserState is "fire"):
            p.fire_laser(p.laserX, p.laserY)
            p.laserY -= p.laserY_Change

        # calls the player movement change
        p.playerX += p.playerX_Change
        # movement boundaries
        if(p.playerX <= 0):
            p.playerX = 0
        elif(p.playerX >= c.SCREEN_WIDTH - 32):
            p.playerX = c.SCREEN_WIDTH - 32

        # calls enemy movement
        e.enemyX += e.enemyX_Change
        # movement boundaries / change direction
        if(e.enemyX <= 0):
            e.enemyX_Change = 4
            e.enemyY += e.enemyY_Change
        elif(e.enemyX >= c.SCREEN_WIDTH - 32):
            e.enemyX_Change = -4
            e.enemyY += e.enemyY_Change

        # calls the player & enemies
        p.player(p.playerX, p.playerY)
        e.enemy(e.enemyX, e.enemyY)

        # updates the screen graphics
        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
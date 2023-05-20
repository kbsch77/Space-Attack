import pygame
import random

import constants as c
import display as d
import player as p
import enemy as e
import score as s
import audio as a

def main():
     
    # initialize the pygame module
    pygame.init()
     
    # define a variable to control the main loop
    running = True

    # background music
    a

    # main loop
    while running:
        #sets background image
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
                    if (p.laserState == "ready"):
                        p.laserX = p.playerX
                        p.fire_laser(p.laserX, p.laserY)
                        a.laserSound()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    p.playerX_Change = 0

        # laser movement
        if (p.laserY <= 0): 
            p.laserY = p.playerY
            p.laserState = "ready"
        if (p.laserState == "fire"):
            p.fire_laser(p.laserX, p.laserY)
            p.laserY -= p.laserY_Change

        # calls the player movement change
        p.playerX += p.playerX_Change
        # movement boundaries
        if(p.playerX <= 0):
            p.playerX = 0
        elif(p.playerX >= c.SCREEN_WIDTH - 32):
            p.playerX = c.SCREEN_WIDTH - 32

        # calls enemy movement for all enemies
        for i in range(e.numofEnemies):
            e.enemyX[i] += e.enemyX_Change[i]
            # movement boundaries / change direction
            if(e.enemyX[i] <= 0):
                e.enemyX_Change[i] = 4
                e.enemyY[i] += e.enemyY_Change[i]
            elif(e.enemyX[i] >= c.SCREEN_WIDTH - 32):
                e.enemyX_Change[i] = -4
                e.enemyY[i] += e.enemyY_Change[i]

            # collision detection
            collision = e.isCollision(e.enemyX[i], e.enemyY[i], p.laserX, p.laserY)
            if collision:
                p.laserY = p.playerY
                p.laserState = "ready"
                s.scoreValue += 1

                # explosion
                a.hitSound()
                e.explode(e.enemyX[i], e.enemyY[i])

                # reset enemy
                e.enemyX[i] = random.randint(1, c.SCREEN_WIDTH - 32)
                e.enemyY[i] = random.randint(50, 400)
                # e.numofEnemies += 1
            
            # calls the enemies
            e.enemy(e.enemyX[i], e.enemyY[i], i)

        # calls the player and score
        p.player(p.playerX, p.playerY)
        s.showScore()

        # updates the screen graphics
        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
import pygame
from pygame import mixer

mixer.music.load('audio/background.wav')
mixer.music.play(-1)

def laserSound():
    laserSound = mixer.Sound('audio/laser.wav')
    laserSound.play()

def hitSound():
    explosionSound = mixer.Sound('audio/explosion.wav')
    explosionSound.play()
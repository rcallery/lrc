import pygame, sys, os
import math, random, time, datetime
from pygame.locals import *

# helper functions
def pellet(num = 1):
    '''Dispense [num] pellets. Defaults to 1.'''
    for i in range(num):
        # subprocess.call('c:/pellet.exe')
        os.system('c:/pellet.exe')

def sound(boolCorr):
    '''If True, play 'correct' sound; if False, play 'incorrect' sound.'''
    if boolCorr:    pygame.mixer.music.load('sounds/correct.wav')
    else:           pygame.mixer.music.load('sounds/incorrect.wav')

    pygame.mixer.music.play()

def quitEscQ():
    '''Quit pygame on QUIT, [Esc], and [Q].'''
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            sys.exit()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600), (pygame.NOFRAME and pygame.FULLSCREEN))
scrRect = pygame.Rect(0, 0, 800, 600)

# hide mouse and initialize joystick
pygame.mouse.set_visible(False)
joy = pygame.joystick.Joystick(0)
joy.init()

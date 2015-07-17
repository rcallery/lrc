import pygame, sys, os
import math, random, time, datetime
from pygame.locals import *

pygame.init()

# load sounds
sndCor = pygame.mixer.Sound('sounds/correct.wav')
sndIncor = pygame.mixer.Sound('sounds/incorrect.wav')

# helper functions
def sound(boolCorr):
    '''If True, play 'correct' sound; if False, play 'incorrect' sound.'''
    if boolCorr:    sndCor.play()
    else:           sndIncor.play()

def pellet(num = 1):
    '''Dispense [num] pellets. Defaults to 1.'''
    for i in range(num):
        os.system('c:/pellet.exe')
        time.sleep(.7)

def quitEscQ():
    '''Quit pygame on QUIT, [Esc], and [Q].'''
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            sys.exit()

screen = pygame.display.set_mode((800, 600), (pygame.NOFRAME and pygame.FULLSCREEN))
scrRect = pygame.Rect(0, 0, 800, 600)

# hide mouse and initialize joystick
pygame.mouse.set_visible(False)
joy = pygame.joystick.Joystick(0)
joy.init()

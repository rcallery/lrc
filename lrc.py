import pygame, sys, os
import math, random, datetime
from pygame.locals import *

pygame.init()

# load sounds
# sndCor = pygame.mixer.Sound('c:/correct.wav')
# sndIncor = pygame.mixer.Sound('c:/incorrect.wav')
# [dev] local copies
sndCor = pygame.mixer.Sound('../correct.wav')
sndIncor = pygame.mixer.Sound('../incorrect.wav')
pelletPath = 'c:/pellet.exe'

# helper functions
def sound(boolCorr):
    '''If True, play whoop (correct.wav); if False, play buzz (incorrect.wav).'''
    if boolCorr:    sndCor.play()
    else:           sndIncor.play()

def pellet(num = 1):
    '''Dispense [num] pellets. Defaults to 1.'''
    if os.path.isfile(pelletPath):
        for i in range(num):
            os.system(pelletPath)
            pygame.time.delay(700)

def quitEscQ():
    '''Quit pygame on QUIT, [Esc], and [Q].'''
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            sys.exit()

screen = pygame.display.set_mode((800, 600), (pygame.NOFRAME and pygame.FULLSCREEN))
scrRect = pygame.Rect(0, 0, 800, 600)

# hide mouse and initialize joystick if available
pygame.mouse.set_visible(False)

joyCount = pygame.joystick.get_count()
if joyCount > 0:
    joy = pygame.joystick.Joystick(0)
    joy.init()

# set cursor speed, size, colour, and start position
cursorSpeed = 8
cursorSize = (20, 20)
cursorCol = (0, 0, 0)
cursorPos = (400, 200)

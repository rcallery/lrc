import pygame, sys, os
import math, random, datetime
from pygame.locals import *

pygame.init()

# load sounds
# [dev] local copies
# sndCor = pygame.mixer.Sound('c:/correct.wav')
# sndIncor = pygame.mixer.Sound('c:/incorrect.wav')
sndCor = pygame.mixer.Sound('../correct.wav')
sndIncor = pygame.mixer.Sound('../incorrect.wav')
pelletPath = 'c:/pellet.exe'

# helper class

class Box(pygame.sprite.Sprite):
    """Class for box with default dimensions (20, 20), in the screen 
       center, black colour, and speed 8."""

    def __init__(self, size = (20, 20), pos = (400, 300), col = (0, 0, 0), speed = 8):
        super(Box, self).__init__()
        self.image = pygame.Surface(size)
        self.image.fill(col)        
        self.rect = self.image.get_rect()
        self.pos = self.rect.center = pos

        self.speed = speed
        self.size = size
        self.col = col

    def update(self):
        self.image.fill(self.col)
        self.rect.center = self.pos

    def move(self, x, y):
        """Move box x pixels to the right and y pixels down. Keep box on-screen."""
        self.rect.move_ip(x * self.speed, y * self.speed)
        self.rect.clamp_ip(scrRect)

    def mv2pos(self, pos):
        """Move box to position (x, y)."""
        self.rect.center = pos

    def collide(self, list):
        """Test if box collides with a rectangle in the list, returns index. 
           Returns -1 when no collision is occuring."""
        return self.rect.collidelist(list)


# helper functions
def sound(boolCorr):
    '''If True, play whoop (correct.wav); if False, play buzz (incorrect.wav).'''
    if boolCorr:    sndCor.play()
    else:           sndIncor.play()

def pellet(num = 1):
    '''Dispense [num] pellets, then wait 700 ms. Defaults to 1.
       Doesn't do anything if it can't find `pellet.exe` (for development).'''
    if os.path.isfile(pelletPath):
        for i in range(num):
            os.system(pelletPath)
            pygame.time.delay(700)

def quitEscQ():
    '''Quit pygame on QUIT, [Esc], and [Q]. Use inside main game loop.'''
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key in (K_ESCAPE, K_q))):
            pygame.quit()
            sys.exit()

def mvCursor(cursor):
    """Move cursor via joystick (if available) or arrow keys (if not).
       Returns boolean that is True when cursor is moving and False when it is not."""
    # no movement unless kb or joystick input
    x_dir = y_dir = 0

    # gets key presses
    key = pygame.key.get_pressed()

    # move cursor with arrow keys
    if joyCount == 0:
        if key[K_LEFT]:    x_dir = -1
        if key[K_RIGHT]:   x_dir = 1
        if key[K_UP]:      y_dir = -1
        if key[K_DOWN]:    y_dir = 1

    # move cursor with joystick
    if joyCount > 0:
        x_dir = round(joy.get_axis(0))
        y_dir = round(joy.get_axis(1))

    cursor.move(x_dir, y_dir)

    if x_dir == y_dir == 0:  return False
    else:                    return True


def getParams(varNames, file = 'parameters.txt'):
    """Read in all even lines from a text file (default 'parameters.txt'). 
        Takes list of strings as argument, creates variables accordingly
        and stores the respective values. Make sure that text values in the
        parameter file are encased in quotes!"""
    txt = open(file)

    for i, line in enumerate(txt):
        if i % 2 == 1:
            j = i / 2
            exec(varNames[j] + '=' + line.strip('\r\n')) in globals()

    txt.close()


screen = pygame.display.set_mode((800, 600), (NOFRAME and FULLSCREEN))
scrRect = pygame.Rect((0, 0), screen.get_size())
bg = pygame.Surface(screen.get_size()).convert()
bg.fill((250, 250, 250))
fps = 60

# hide mouse and initialize joystick if available
pygame.mouse.set_visible(False)

joyCount = pygame.joystick.get_count()
if joyCount > 0:
    joy = pygame.joystick.Joystick(0)
    joy.init()
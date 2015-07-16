#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, time, subprocess
from pygame.locals import *

# USER INPUT
# ----------

# set cursor speed, size, colour, and start position
cursorSpeed = 8
cursorSize = (25, 25)
cursorPos = (400, 200)


# ----------

pygame.init()
pygame.mixer.init()

# helper functions
def pellet():
    subprocess.call("c:/pellet.exe")
    time.sleep(.7)

def sound(boolCorr):
	if boolCorr:	pygame.mixer.music.load('sounds/correct.wav')
	else:			pygame.mixer.music.load('sounds/incorrect.wav')
	
	pygame.mixer.music.play()


screen = pygame.display.set_mode((800, 600), (pygame.NOFRAME and pygame.FULLSCREEN))
scrRect = pygame.Rect(0, 0, 800, 600)

# hide mouse and initialize joystick
pygame.mouse.set_visible(False)
joy = pygame.joystick.Joystick(0)
joy.init()

# define cursor
cursor = pygame.Rect((0, 0), cursorSize)
cursor.center = cursorPos

# define incorrect and correct buttons
corRect = pygame.Rect((0, 0), (150, 80))
corRect.center = (200, 400)
incorRect = pygame.Rect((0, 0), (150, 80))
incorRect.center = (600, 400)

clock = pygame.time.Clock()


while True:
    # quit on QUIT, [Esc], and [Q]
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            sys.exit()

    # move cursor
    h_axis_pos = round(joy.get_axis(0), 5)
    v_axis_pos = round(joy.get_axis(1), 5)
    cursor.move_ip(h_axis_pos * cursorSpeed, 
                   v_axis_pos * cursorSpeed)

    # keep cursor on-screen
    cursor.clamp_ip(scrRect)

    if cursor.colliderect(corRect):
    	pellet()
    	sound(True)
    	cursor.center = cursorPos
    elif cursor.colliderect(incorRect):
    	sound(False)
    	cursor.center = cursorPos

    # update screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (117, 227, 111), corRect)
    pygame.draw.rect(screen, (232, 70, 70), incorRect)
    pygame.draw.rect(screen, (0, 0, 0), cursor)
    pygame.display.update()

    # frame rate
    clock.tick(60)

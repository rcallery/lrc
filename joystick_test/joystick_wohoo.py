#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, subprocess, time
from pygame.locals import *

# helper function
def pellet():
    subprocess.call("c:/pellet.exe")
    time.sleep(.7)


pygame.init()

# for fullscreen, add:  (pygame.NOFRAME and pygame.FULLSCREEN)
screen = pygame.display.set_mode((800, 450))

# initialize joystick
joy = pygame.joystick.Joystick(0)
joy.init()

# set cursor speed
cursorSpeed = 10

# set start position
x = 385
y = 210

# load images
crosshairs = pygame.image.load("crosshairs.png")
background = pygame.image.load("background.jpg")

# set rectangles for images
Cursor = pygame.Rect(x, y, 30, 30)
Back = pygame.Rect(0, 0, 800, 450)

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            sys.exit()
            # break

    h_axis_pos = round(joy.get_axis(0), 5)
    v_axis_pos = round(joy.get_axis(1), 5)
    
    # update position
    x += int(h_axis_pos * cursorSpeed)
    y += int(v_axis_pos * cursorSpeed)

    Cursor.left = x
    Cursor.top = y

    # keep cursor from going off-screen
    if x < 0:       x = 0
    elif x > 770:   x = 770
    if y < 0:       y = 0
    elif y > 420:   y = 420

    # screen.fill(WHITE)

    screen.blit(background, Back)
    screen.blit(crosshairs, Cursor)

    pygame.display.update()
    clock.tick(20)
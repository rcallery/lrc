#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 450))

# initialize joystick
joy = pygame.joystick.Joystick(0)
joy.init()

# hide mouse
pygame.mouse.set_visible(False)

# set cursor speed
cursorSpeed = 5

# load images
crosshairs = pygame.image.load("crosshairs.png")
background = pygame.image.load("background.jpg")

# set rectangles for images
cursor = pygame.Rect(385, 210, 30, 30)
scrRect = pygame.Rect(0, 0, 800, 450)

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

    # update screen
    screen.blit(background, scrRect)
    screen.blit(crosshairs, cursor)
    pygame.display.update()

    # frame rate
    clock.tick(60)

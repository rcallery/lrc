#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
import subprocess
import time


def pellet():
    subprocess.call("c:/pellet.exe")
    time.sleep(.7)

pygame.init()

windowSurface = pygame.display.set_mode((800, 450), 0, 32)

joystick_count = pygame.joystick.get_count()
print "There is ", joystick_count, "joystick/s."
if joystick_count == 0:
    print "Error: No joystick found."
else:
    joy = pygame.joystick.Joystick(0)
    joy.init()

crosshairs = pygame.image.load("crosshairs.png")
background = pygame.image.load("background.jpg")

x = 385
y = 210

Rectangle = pygame.Rect(x, y, 30, 30)
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
    # print (h_axis_pos, v_axis_pos)

    if x < 0 and h_axis_pos < 0:
        h_axis_pos = 0
    elif x > 770 and h_axis_pos > 0:
        h_axis_pos = 0
    
    if y < 0 and v_axis_pos < 0:
        v_axis_pos = 0
    elif y > 420 and v_axis_pos > 0:
        v_axis_pos = 0

    # _axis_pos*[speed_of_cursor]
    x += int(h_axis_pos*10)
    y += int(v_axis_pos*10)

    # print 'Position:', x+15, y+15
    Rectangle.left = x
    Rectangle.top = y

    ###windowSurface.fill(WHITE)

    windowSurface.blit(background, Back)
    windowSurface.blit(crosshairs, Rectangle)

    pygame.display.update()
    clock.tick(20)

# pygame.quit()
# sys.exit()

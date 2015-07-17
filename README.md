# LRC Python Experiments

## lrc.py

Have these files in `C:/`
- lrc.py
- pellet.exe
- correct.wav
- incorrect.wav

Add these lines at the top of your .py script:

	import imp
	lrc = imp.load_source('lrc', 'c:/lrc.py')
	from lrc import *

- imports modules
  - pygame, pygame.locals
  - sys, os
  - math, random, time, datetime
- defines helper functions
  - `pellet(num)`: Dispenses [num] pellets, then waits 700 ms. Defaults to 1 pellet.
  - `sound(boolCorr)`: If True, play whoop (correct.wav); if False, play buzz (incorrect.wav).
  - `quitEscQ()`: Quit pygame on QUIT, [Esc], and [Q]. (Use inside main game loop.)
- initialises pygame
- sets `screen` as 800x600, fullscreen, no frame
- defines `scrRect` to match screen
- hides mouse cursor
- initialises joystick as `joy`

## systemCheck

- use joystick to select one of two buttons
- resets cursor to start position
  - green button plays sounds/correct.wav and dispenses three pellets
  - red button plays sounds/incorrect.wav

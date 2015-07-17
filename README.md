# LRC Python Experiments

## LRC Toolbox - lrc.py

Have these files in `C:/`
- lrc.py
- pellet.exe
- correct.wav
- incorrect.wav

Add these lines at the top of your .py script:

	import imp
	lrc = imp.load_source('lrc', 'c:/lrc.py')
	from lrc import *

* * *

- Imports modules
  + pygame, pygame.locals
  + sys, os
  + math, random, time, datetime
- Defines helper functions
  + `pellet(num)`: Dispense [num] pellets, then waits 700 ms. Defaults to 1 pellet. Doesn't do anything if it can't find `pellet.exe` (for development).
  + `sound(boolCorr)`: If True, play whoop (correct.wav); if False, play buzz (incorrect.wav).
  + `quitEscQ()`: Quit pygame on QUIT, [Esc], and [Q]. (Use inside main game loop.)
- Initialises pygame
- Sets `screen` to 800x600 resolution, fullscreen, no frame
- Defines rectangle `scrRect` with screen dimensions
- Sets frame rate to `fps = 60` frames per second
- Hides mouse cursor
- Returns `joyCount = 0` if it can't find a joystick. Initialises joystick as `joy` if available
- Sets cursor defaults
  + `cursorSpeed = 8` - number of pixels moved per frame
  + `cursorSize = (20, 20)` - (width, height) in pixels
  + `cursorCol = (0, 0, 0)` - black
  + `cursorPos = (400, 200)` - (x, y) coordinates in pixels

## systemCheck

- Use joystick (if available) or arrow keys (if not) to select one of two buttons
- Resets cursor to start position
  + Green button plays sounds/correct.wav and dispenses three pellets
  + Red button plays sounds/incorrect.wav

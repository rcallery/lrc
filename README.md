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
  + math, random, datetime
- Initialises pygame
- Defines helper class `Box` with these defaults (for the cursor):
  + `size = (20, 20)` - (width, height) in pixels
  + `pos = (400, 300)` - (x, y) center coordinates in pixels
  + `col = (0, 0, 0)` - black 
  + `speed = 8` - number of pixels moved per frame
  + Functions
    * `move(x, y)` - Move box `x` pixels to the right and `y` pixels down. Keep box on-screen.
    * `mv2pos(pos)` - Move box to position `(x, y)`.
    * `collide(list)` - Test if box collides with a rectangle in the list, returns index. Returns `-1` when no collision is occuring.
- Defines helper functions
  + `sound(boolCorr)`: If True, play whoop (correct.wav); if False, play buzz (incorrect.wav).
  + `pellet(num)`: Dispense [num] pellets, then wait 700 ms. Defaults to 1 pellet. Doesn't do anything if it can't find `pellet.exe` (for development).
  + `quitEscQ()`: Quit pygame on QUIT, [Esc], and [Q]. (Use inside main game loop.)
  + `mvCursor(cursor)` - Move cursor via joystick (if available) or arrow keys (if not). Returns boolean that is True when cursor is moving and False when it is not.
  + `getParams(varNames, files = 'parameters.txt')` - Read in all odd lines from a text file (default 'parameters.txt'). Takes list of strings as argument, creates variables accordingly and stores the respective values. It is important that strings in the parameter file are encased in quotes!
- Sets `screen` to `800x600` resolution, fullscreen, no frame
- Defines rectangle `scrRect` with screen dimensions
- Defines `bg` background surface object with screen dimensions and off-white (250, 250, 250) colour.
- Sets frame rate to `fps = 60` frames per second
- Hides mouse cursor
- Returns `joyCount = 0` if it can't find a joystick. Initialises joystick as `joy` if available

## systemCheck

- Select one of two buttons
  + Green button plays sounds/correct.wav and dispenses three pellets
  + Red button plays sounds/incorrect.wav
- Reset cursor to start position
- Key presses:
  + [p]: dispenses pellet
  + [s]: plays whoop (correct.wav)

## chase

Chase target with cursor.

- Target only moves when cursor moves
- Target changes direction when it reaches the screen border
- Catching target
  + Plays whoop
  + Dispenses a pellet
  + Resets target with random 
    - Position
    - Colour (out of six presets)
    - Direction (out of the eight compass directions)
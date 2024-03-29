# LRC Python Experiments

## LRC Toolbox - lrc.py

Have these files in `C:/`
- `lrc.py`
- `pellet.exe`
- `correct.wav`
- `incorrect.wav`

Other files
- `MonkeyName.txt` - default folder: `C:/`
- `parameters.txt` - default folder: same as your script

Add these lines at the top of your .py script:

	import imp
	lrc = imp.load_source('lrc', 'c:/lrc.py')
	from lrc import *

* * *

- Imports modules
  + pygame, pygame.locals
  + sys, os
  + math, random, time
- Initialises pygame
- Pre-defines colour dictionary:
  + white, black, purple, blue, red, green, yellow, orange
  + Use with `cols['colour name']`
- Sets `scrSize` to `800x600` resolution
- `setScreen()` - Return display with screen dimensions, no frame, and fullscreen. 
  (Assign to variable.)
- Defines rectangle `scrRect` with screen dimensions
- Defines `bg` background surface object with screen dimensions and white colour.
- Sets frame rate to `fps = 60` frames per second
- Hides mouse cursor
- Returns `joyCount = 0` if it can't find a joystick. Initialises joystick as `joy` if available

### Defines helper class `Box`

Defaults (for the cursor):
- `size = (20, 20)` - (width, height) in pixels
- `pos = (400, 300)` - (x, y) center coordinates in pixels
- `col = (0, 0, 0)` - black 
- `speed = 8` - number of pixels moved per frame
- Functions
  + `update()` - Update colour and position.
  + `draw(surface)` - Draw box onto `surface`. (Pass display/screen object assigned with `setScreen()`.)
  + `move(x, y)` - Move box `x` pixels to the right and `y` pixels down. Keep box on-screen.
  + `mv2pos(pos)` - Move box to position `(x, y)`.
  + `collide(list)` - Test if box collides with a rectangle in the list, returns index. Returns `-1` when no collision is occuring.

### Defines helper functions
- `sound(boolCorr)`: If True, play whoop (correct.wav); if False, play buzz (incorrect.wav).
- `pellet(num)`: Dispense [num] pellets, then wait 700 ms. Defaults to 1 pellet. Doesn't do anything if it can't find `pellet.exe` (for development).
- `quitEscQ()`: Quit pygame on QUIT, [Esc], and [Q]. (Use inside main game loop.)
- `mvCursor(cursor)` - Move cursor via joystick (if available) or arrow keys (if not). Returns boolean that is True when cursor is moving and False when it is not.
- `getParams(varNames, file = 'parameters.txt')` - Read in all even lines from a text file (default 'parameters.txt'). 
        Takes list of variable names as argument and stores them with
        their values. Returns a dictionary. *Make sure that text values in the parameter file are encased in quotes!*
  + The dictionary can then be converted into variables:
    
    ```
    var = ['var1', 'var2', 'var3', 'var4]
    parameters = getParams(var)
    globals().update(parameters)
    ```

- `makeFileName(file = 'c:/MonkeyName.txt', task = 'Task')` - Read monkey name from file (default: `c:/MonkeyName.txt`). Argument task takes the task name (encased in quotes). Get current date. Return string of form `MonkeyName_Task_YYYY-MM-DD.txt`.

* * *

## template

This is a minimal working example. It creates a default display with a default cursor, which is controlled via joystick (if available) or mouse (if not).

## systemCheck

- Select one of two buttons
  + Green button plays sounds/correct.wav and dispenses three pellets
  + Red button plays sounds/incorrect.wav
- Reset cursor to start position
- Key presses:
  + [p]: dispenses pellet
  + [s]: plays whoop (correct.wav)

## chase

Toolbox implementation of chase

- Target only moves when cursor moves
- Target changes direction when it reaches the screen border
- Catching target
  + Plays whoop
  + Dispenses a pellet
  + Resets target with random 
    - Position
    - Colour (out of six presets)
    - Direction (out of the eight compass directions)
- Choice of dark or light theme (black cursor on white or vice versa) ;)
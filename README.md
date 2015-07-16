# LRC Python Experiments

## lrc.py

Use by adding these lines at the top of your .py script.
You only need the last line if lrc.py is in the same folder as your script.

	import imp
	lrc = imp.load_source('lrc', '../lrc.py')

	from lrc import *

- imports modules: pygame, pygame.locals, sys, os time
- defines helper functions
  - `pellet(num)`: Dispenses [num] pellets. Defaults to 1.
  - `sound(boolCorr)`: If True, play 'correct' sound; if False, play 'incorrect' sound.
  - `quitEscQ()`: Quit pygame on QUIT, [Esc], and [Q]. (Use inside main game loop.)
- initialises pygame, pygame.mixer
- sets `screen` as (800, 600), fullscreen, no frame
- defines `scrRect` to match screen
- hides mouse cursor
- initialises joystick as `joy`

## joystickTest

Joystick moves cursor (crosshairs.png) on window with background.jpg

## systemCheck

- use joystick select one of two buttons
- resets cursor to start position
  - red button plays sounds/incorrect.wav
  - green button plays sounds/correct.wav and dispenses a pellet

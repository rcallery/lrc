# LRC Python Experiments

## joystickTest

Joystick moves cursor (crosshairs.png) on window with background.jpg

## systemCheck

- defines helper functions
  - pellet(num): Dispenses [num] pellets. Defaults to 1.
  - sound(boolCorr): If True, play 'correct' sound; if False, play 'incorrect' sound.
  - quitEscQ(): Quit pygame on QUIT, [Esc], and [Q]. (Use inside main game loop.)
- hides mouse cursor
- use joystick select one of two buttons
- resets cursor to start position
  - red button plays sounds/incorrect.wav
  - green button plays sounds/correct.wav and dispenses a pellet
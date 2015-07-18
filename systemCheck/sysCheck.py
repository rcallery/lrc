import imp
# lrc = imp.load_source('lrc', 'c:/lrc.py')
# [dev] local copy
lrc = imp.load_source('lrc', '../lrc.py')

from lrc import *

# define cursor
cursor = pygame.Rect((0, 0), cursorSize)
cursor.center = cursorPos

# define incorrect and correct buttons
corRect = pygame.Rect((0, 0), (150, 80))
corRect.center = (200, 400)
incorRect = pygame.Rect((0, 0), (150, 80))
incorRect.center = (600, 400)

clock = pygame.time.Clock()

# add text to background
font = pygame.font.Font(None, 36)
text = font.render('Press [p] for pellet, [s] for sound.', 1, (10, 10, 10))
textpos = text.get_rect(centerx = bg.get_width() / 2, y = 15)
bg.blit(text, textpos)

while True:
    # quit on QUIT, [Esc], and [Q]
    quitEscQ()

    # gets key presses
    key = pygame.key.get_pressed()

    # dispense pellet if [p] is pressed
    if key[K_p]:    pellet()
    if key[K_s]:    sound(True)

    # no movement unless kb or joystick input
    h_axis_pos = v_axis_pos = 0

    # move cursor with arrow keys (if joystick unavailable)
    if joyCount == 0:
        if key[K_LEFT]:    h_axis_pos = -1
        if key[K_RIGHT]:   h_axis_pos = 1
        if key[K_UP]:      v_axis_pos = -1
        if key[K_DOWN]:    v_axis_pos = 1

    # move cursor with joystick (if available)
    if joyCount > 0:
        h_axis_pos = round(joy.get_axis(0))
        v_axis_pos = round(joy.get_axis(1))

    cursor.move_ip(h_axis_pos * cursorSpeed, 
                   v_axis_pos * cursorSpeed)

    # keep cursor on-screen
    cursor.clamp_ip(scrRect)

    if cursor.colliderect(corRect):
        sound(True)
        cursor.center = cursorPos
        pellet(3)
    elif cursor.colliderect(incorRect):
        sound(False)
        cursor.center = cursorPos

    # update screen
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, (117, 227, 111), corRect)
    pygame.draw.rect(screen, (232, 70, 70), incorRect)
    pygame.draw.rect(screen, cursorCol, cursor)
    pygame.display.flip()
    # pygame.display.update()

    # frame rate
    clock.tick(fps)

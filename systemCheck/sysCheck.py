# delete these two lines if lrc.py is in the same folder
import imp
lrc = imp.load_source('lrc', '../lrc.py')

from lrc import *

# set cursor speed, size, colour, and start position
cursorSpeed = 8
cursorSize = (25, 25)
cursorPos = (400, 200)

# for developing purposes (not fullscreen, with frame)
# screen = pygame.display.set_mode((800, 600))

# define cursor
cursor = pygame.Rect((0, 0), cursorSize)
cursor.center = cursorPos

# define incorrect and correct buttons
corRect = pygame.Rect((0, 0), (150, 80))
corRect.center = (200, 400)
incorRect = pygame.Rect((0, 0), (150, 80))
incorRect.center = (600, 400)

clock = pygame.time.Clock()


while True:
    # quit on QUIT, [Esc], and [Q]
    quitEscQ()

    # move cursor
    h_axis_pos = round(joy.get_axis(0))
    v_axis_pos = round(joy.get_axis(1))
    cursor.move_ip(h_axis_pos * cursorSpeed, 
                   v_axis_pos * cursorSpeed)

    # keep cursor on-screen
    cursor.clamp_ip(scrRect)

    if cursor.colliderect(corRect):
        sound(True)
        pellet(3)
        cursor.center = cursorPos
    elif cursor.colliderect(incorRect):
        sound(False)
        cursor.center = cursorPos

    # update screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (117, 227, 111), corRect)
    pygame.draw.rect(screen, (232, 70, 70), incorRect)
    pygame.draw.rect(screen, (0, 0, 0), cursor)
    pygame.display.update()

    # frame rate
    clock.tick(60)

import imp
# lrc = imp.load_source('lrc', 'c:/lrc.py')
# [dev] local copy
lrc = imp.load_source('lrc', '../lrc.py')
from lrc import *

# set screen; define cursor
screen = setScreen()
cursor = Box()

clock = pygame.time.Clock()

while True:
    quitEscQ()
    mvCursor(cursor)

    # update screen
    screen.blit(bg, (0, 0))
    screen.blit(cursor.image, cursor.rect)
    pygame.display.update()
    clock.tick(fps)
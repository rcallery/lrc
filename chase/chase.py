import imp
# lrc = imp.load_source('lrc', 'c:/lrc.py')
# [dev] local copy
lrc = imp.load_source('lrc', '../lrc.py')

from lrc import *

# set screen; define cursor
screen = setScreen()

# dark theme
# bg.fill((0, 0, 0))
# cursor = Box(col = (250, 250, 250))

# light theme
bg.fill((250, 250, 250))
cursor = Box()

# target colors
cols = {'purple': (154,  55, 219),
        'blue':   (  7, 147, 235),
        'red':    (232,  70,  70),
        'green':  (117, 227, 111),
        'yellow': (255, 239,   0),
        'orange': (255, 128,   0)}

def pickCol():
    return random.choice(cols.values())

def pickPos():
    x = random.randrange(25, 775)
    y = random.randrange(25, 575)
    return (x, y)

def pickDir():
    x_dir = y_dir = 0
    while x_dir == y_dir == 0:
        x_dir = random.randrange(3) - 1
        y_dir = random.randrange(3) - 1
    return x_dir, y_dir

# define target
target = Box((50, 50), pickPos(), pickCol(), speed = 5)
tx_dir, ty_dir = pickDir()

clock = pygame.time.Clock()

while True:
    quitEscQ()
    cursorMoving = mvCursor(cursor)

    if cursorMoving:
        target.move(tx_dir, ty_dir)

    # pick new direction when target reaches screen border
    if target.rect.top == scrRect.top or \
        target.rect.bottom == scrRect.bottom or \
        target.rect.right == scrRect.right or \
        target.rect.left == scrRect.left:

        tx_dir, ty_dir = pickDir()

    # if cursor catches target
    if cursor.collide([target]) == 0:
        sound(True)
        pellet()
        
        # pick new target colour, position, and direction
        target.pos = pickPos()
        target.col = pickCol()
        tx_dir, ty_dir = pickDir()
        target.update()

    # update screen
    screen.blit(bg, (0, 0))
    screen.blit(cursor.image, cursor.rect)
    screen.blit(target.image, target.rect)
    pygame.display.update()

    # frame rate
    clock.tick(fps)

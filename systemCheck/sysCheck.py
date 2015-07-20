import imp
# lrc = imp.load_source('lrc', 'c:/lrc.py')
# [dev] local copy
lrc = imp.load_source('lrc', '../lrc.py')

from lrc import *

# define cursor with start position
initPos = (400, 200)
cursor = Box(pos = initPos)

# define correct and incorrect buttons
boxes = [Box((150, 80), (600, 400), (232, 70, 70)),
         Box((150, 80), (200, 400), (117, 227, 111))]

# add text to background
font = pygame.font.Font(None, 36)
text = font.render('Press [p] for pellet, [s] for sound.', 1, (10, 10, 10))
textpos = text.get_rect(centerx = bg.get_width() / 2, y = 15)
bg.blit(text, textpos)

clock = pygame.time.Clock()

while True:
    # quit on QUIT, [Esc], and [Q]
    quitEscQ()

    # gets key presses
    key = pygame.key.get_pressed()

    # [p] dispenses pellet
    if key[K_p]:
        pellet()
        pygame.time.delay(300)

    # [s] plays whoop (correct.wav)
    if key[K_s]:
        sound(True)
        pygame.time.delay(300)

    # move cursor (with joystick or kb)
    mvCursor(cursor)

    # return index of colliding box
    select = cursor.collide(boxes)

    if select == 0:
        sound(False)
        cursor.mv2pos(initPos)
    elif select == 1:
        sound(True)
        cursor.mv2pos(initPos)
        pellet(3)

    # update screen
    screen.blit(bg, (0, 0))
    screen.blit(cursor.image, cursor.rect)
    for box in boxes:   screen.blit(box.image, box.rect)
    pygame.display.update()

    # frame rate
    clock.tick(fps)

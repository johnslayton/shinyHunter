import pydirectinput
from time import sleep, time
from detect import *
import threading
import msvcrt

# walking
def moveGrassTile(num, direction):
    walk = 0.3
    pydirectinput.keyDown(direction)
    sleep(walk * (num - 2))
    pydirectinput.keyUp(direction)
    sleep(.1)

def runGrassTile(num, direction):
    run = 0.15
    # pydirectinput.keyDown('z')
    pydirectinput.keyDown(direction)
    sleep(run * (num - 2))
    pydirectinput.keyUp(direction)
    sleep(.05)
    # pydirectinput.keyUp('z')
    # sleep(.05)


def move_right(num_tiles, speed=0):
    if speed == 1:
        runGrassTile(num_tiles, 'd')
    else:
        moveGrassTile(num_tiles, 'd')


def move_left(num_tiles, speed=1):
    if speed == 1:
        runGrassTile(num_tiles, 'a')
    else:
        moveGrassTile(num_tiles, 'a')

# sleep(2)
# pydirectinput.keyDown('z')
# while 1:
#     # moveGrassTile(6, 'd')
#     # moveGrassTile(6, 'a')
    
#     runGrassTile(9, 'd')
#     runGrassTile(9, 'a')
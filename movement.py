import pydirectinput
from time import sleep, time
from detect import *
import threading
import msvcrt

# walking
def moveGrassTile(num, direction, speed):
    walk = 0.29
    pydirectinput.keyDown(direction)
    sleep(walk * (num - 1))
    pydirectinput.keyUp(direction)
    sleep(.25)

def runGrassTile(num, direction):
    run = 0.15
    pydirectinput.keyDown('z')
    pydirectinput.keyDown(direction)
    sleep(run * (num - 1))
    pydirectinput.keyUp(direction)
    pydirectinput.keyUp('z')
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

sleep(2)
while 1:
    runGrassTile(4, 'd')
    runGrassTile(4, 'a')
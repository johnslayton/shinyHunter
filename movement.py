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
    pydirectinput.keyDown(direction)
    sleep(run * (num - 2))
    pydirectinput.keyUp(direction)
    sleep(.1)

# sleep(2)
# pydirectinput.keyDown('z')
# while 1:
#     # moveGrassTile(6, 'd')
#     # moveGrassTile(6, 'a')
    
#     runGrassTile(9, 'd')
#     runGrassTile(9, 'a')
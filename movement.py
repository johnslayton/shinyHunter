import pydirectinput
from time import sleep, time
from detect import *
import threading
import msvcrt

# walking
def moveGrassTile(num, direction):
    t = 0.29
    pydirectinput.keyDown(direction)
    sleep(t * (num - 1))
    pydirectinput.keyUp(direction)
    sleep(.25)

# moveGrassTile(1, 'd')

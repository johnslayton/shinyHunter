import pydirectinput
from time import sleep
from detect import *
# spoof input for encounter
# face down, need 3 grass
# go until encounter


def grass_encounter():
    # TODO: do vertical or horizontal
    # take input for dimensions
    # could do image for determining where character is or input idk
    # probably start a thread that is constantly checking for an encounter
    print("grass")
    i = 0
    sleep(2)
    pydirectinput.keyDown('z')
    while i <= 30:
        pydirectinput.press("w")
        sleep(.2)
        if detect():
            break
        pydirectinput.press('s')
        sleep(.2)
        if detect():
            break
        pydirectinput.press('s')
        sleep(.2)
        if detect():
            break
        pydirectinput.press('s')
        sleep(.2)
        if detect():
            break
        pydirectinput.press('w')
        sleep(.2)
        if detect():
            break
        pydirectinput.press('w')
        sleep(.2)
        if detect():
            break
        pydirectinput.press('w')
        if detect():
            break
        # detect()
        i += 1
    # pydirectinput.press('w')
    print('wild pokemon appeared')

grass_encounter()
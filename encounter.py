import pydirectinput
from time import sleep, time
from detect import *
import threading
import msvcrt
# spoof input for encounter
# face down, need 3 grass
# go until encounter

encounter_flag = threading.Event()


aborted = False
def wild_encounter():
    while not encounter_flag.is_set():
        if detect_wild() or (msvcrt.kbhit() and msvcrt.getch() == chr(27).encode()):
            encounter_flag.set()

def shiny_detect():
    print("sparkles")

def circle_encounter():
    timeout = 30
    start_time = time()
    # pydirectinput.keyDown('z')
    sleep(2)
    while not encounter_flag.is_set():
        pydirectinput.keyDown("w")
        sleep(.0001)
        pydirectinput.keyUp("w")
        sleep(.0001)
        pydirectinput.keyDown("a")
        sleep(.0001)
        pydirectinput.keyUp("a")
        sleep(.0001)
        pydirectinput.keyDown("s")
        sleep(.0001)
        pydirectinput.keyUp("s")
        sleep(.0001)
        pydirectinput.keyDown("d")
        sleep(.0001)
        pydirectinput.keyUp("d")
        sleep(.0001)
        # Check if the timeout has been reached
        elapsed_time = time() - start_time
        if elapsed_time >= timeout:
            break

def grass_encounter():
    # TODO: do vertical or horizontal
    # take input for dimensions
    # could do image for determining where character is or input idk
    # probably start a thread that is constantly checking for an encounter
    # print("grass")
    # i = 0
    # sleep(2)
    timeout = 30
    start_time = time()
    # pydirectinput.keyDown('z')
    while not encounter_flag.is_set():
        pydirectinput.press("w")
        sleep(.2)
        # if detect():
            # break
        pydirectinput.press('s')
        sleep(.2)
        # if detect():
            # break
        pydirectinput.press('s')
        sleep(.2)
        # if detect():
            # break
        pydirectinput.press('s')
        sleep(.2)
        # if detect():
            # break
        pydirectinput.press('w')
        sleep(.2)
        # if detect():
            # break
        pydirectinput.press('w')
        sleep(.2)
        # if detect():
        #     break
        pydirectinput.press('w')
        # Check if the timeout has been reached
        elapsed_time = time() - start_time
        if elapsed_time >= timeout:
            break
        # if detect():
        #     break
        # detect()
        # i += 1
    # pydirectinput.press('w')
    # encounter_flag.is_set()



def leave():
    # press a
    print("leave")
    pydirectinput.press('w')
    pydirectinput.press('a')
    pydirectinput.press('x')
    sleep(2)
    pydirectinput.press('s')
    pydirectinput.press('d')
    pydirectinput.press('x')
    sleep(2)
    pydirectinput.press('x')


def encounter():
    # sleep(1)
    t1 = threading.Thread(target=wild_encounter, name='t1')
    t2 = threading.Thread(target=circle_encounter, name='t2') 
    t3 = threading.Thread(target=leave, name='t3') 
    t1.start()
    t2.start()
    
    # wait until all threads finish
    t1.join()
    # t2.join()
    # encounter_flag.set()
    t2.join()
    if detect_template('sma'):
        print('asdf')
    else:
        print('qwer')
        t3.start()
        t3.join()

circle_encounter()

import pydirectinput
from time import sleep, time
from detect import *
import threading
# spoof input for encounter
# face down, need 3 grass
# go until encounter

encounter_flag = threading.Event()

def wild_encounter():
    while not encounter_flag.is_set():
        if detect_wild():
            encounter_flag.set()

def shiny_detect():
    print("sparkles")

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

def encounter():
    sleep(2)
    t1 = threading.Thread(target=wild_encounter, name='t1')
    t2 = threading.Thread(target=grass_encounter, name='t2') 
    t1.start()
    t2.start()
 
    # wait until all threads finish
    t1.join()
    # t2.join()
    # encounter_flag.set()
    t2.join()
    print('wild detected')
    if detect_template('smarill'):
        print('shiny')
    else:
        print('not shiny')



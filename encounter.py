import pydirectinput
from time import sleep, time
from detect import *
import threading
import msvcrt
from movement import *
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


# TODO: currently have to face not direction you're running
# when starting
def grass_encounter(distance, direction):
    # TODO: do vertical or horizontal
    # take input for dimensions
    # could do image for determining where character is or input idk
    # probably start a thread that is constantly checking for an encounter
    # print("grass")
    # i = 0
    # sleep(2)
    timeout = 30
    start_time = time()
    pydirectinput.keyDown('z')
    routes = {  "right-left": ['d', 'a'],
                "left-right": ['a', 'd'],
                'up-down': ['w', 's'],
                'down-up':['s', 'w']
              }
    route = routes[direction]
    while not encounter_flag.is_set():
        runGrassTile(distance, route[0])
        # runGrassTile(distance, 'd')
        runGrassTile(distance, route[1])
        # runGrassTile(distance, 'a')
        elapsed_time = time() - start_time
        if elapsed_time >= timeout:
            pydirectinput.keyUp('z')
            break


def leave():
    # press a
    print("leave")
    sleep(3)
    # TODO: abilities delay input, so gotta figure that out
    pydirectinput.press('x')
    sleep(6)
    pydirectinput.press('s')
    pydirectinput.press('d')
    pydirectinput.press('x')
    sleep(1)
    pydirectinput.press('x')
    sleep(2)

# TODO: thread that will close out of popups
def encounter(dist, direction):
    # sleep(1)
    t1 = threading.Thread(target=wild_encounter, name='t1')
    # t2 = threading.Thread(target=circle_encounter, name='t2') 
    t2 = threading.Thread(target=grass_encounter,args={dist, direction},name='t2') 
    t3 = threading.Thread(target=leave, name='t3') 
    # pydirectinput.keyDown('z')
    t1.start()
    t2.start()
    
    # wait until all threads finish
    t1.join()
    # t2.join()
    # encounter_flag.set()
    t2.join()
    if detect_template('smarill'):
        print('smarill spotted')
    else:
        print('nah')
        t3.start()
        t3.join()

# circle_encounter()

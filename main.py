from window import *
from encounter import *
import pydirectinput
from time import sleep, time
import keyboard
dimensions = [1200, 800]



import msvcrt



def startup():
    # sets dimensions of window
    getDimensions()
    # initialize pydirectinput
    pydirectinput.FAILSAFE = True

def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(.25)
    print("Go")

def main():
    # TODO: input from user, up and down, left and right, how many, etc.
    countdownTimer()
    startup()     
    # while 1
    # gonna need a keyboard interupt
    # aborted = False
    # while not aborted:
    #     if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
    #         aborted = True
    #         break
    encounter()

if __name__ == '__main__':
    main()
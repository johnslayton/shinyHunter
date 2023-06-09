from window import *
from encounter import *
import pydirectinput
from time import sleep, time

dimensions = [1200, 800]

def startup():
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
    countdownTimer()
    startup()    
    grass_encounter()

if __name__ == '__main__':
    main()
from window import *
from encounter import *
import pydirectinput
from time import sleep, time
import keyboard
import tkinter as tk
import msvcrt

dimensions = [1200, 800]

def winput(title, sentence):
    import tkinter as tk
    from tkinter import simpledialog
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y



# class Example(tk.Frame):
#     def __init__(self, parent):
#         tk.Frame.__init__(self, parent)

#         # create a prompt, an input box, an output label,
#         # and a button to do the computation
#         self.prompt = tk.Label(self, text="Enter a number:", anchor="w")
#         self.entry = tk.Entry(self)
#         self.submit = tk.Button(self, text="Submit", command = self.calculate)
#         self.output = tk.Label(self, text="")

#         # lay the widgets out on the screen. 
#         self.prompt.pack(side="top", fill="x")
#         self.entry.pack(side="top", fill="x", padx=20)
#         self.output.pack(side="top", fill="x", expand=True)
#         self.submit.pack(side="right")

#     def calculate(self):
#         # get the value from the input widget, convert
#         # it to an int, and do a calculation
#         try:
#             i = int(self.entry.get())
#             result = "%s*2=%s" % (i, i*2)
#         except ValueError:
#             result = "Please enter digits only"

#         # set the output widget to have our result
#         self.output.configure(text=result)



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
    dist = winput("What distance are you running")
    direction = winput("What direction are you running?")
    # TODO: input from user, up and down, left and right, how many, etc.
    countdownTimer()
    startup()
    # while 1
    # gonna need a keyboard interupt
    encounter(direction, dist)

if __name__ == '__main__':
    main()
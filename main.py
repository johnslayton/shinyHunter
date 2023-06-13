from window import *
from encounter import *
import pydirectinput
from time import sleep, time
import keyboard
import tkinter as tk
import msvcrt
from tkinter import simpledialog, ttk
from tkinter import *

dimensions = [1200, 800]




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


def winput(title, sentence):
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y



# Dropdown menu options
options = [
    "right-left",
    "left-right",
    "up-down",
    "down-up"
]

     
def main():

    # declaring string variable
    # for storing name and password

    #Create an instance of Tkinter frame
    win= Tk()
    #Set the geometry of Tkinter frame
    win.geometry("750x250")
    win.title("Hunter Input")
    num_var=tk.IntVar()
    way_var=tk.StringVar()
    def submit():
        global dist
        global direction
        dist=num_var.get()
        direction=way_var.get()
        win.destroy()

    # creating a label for
    # name using widget Label
    name_label = tk.Label(win, text = 'Distance', font=('calibre',10, 'bold'))
    
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(win,textvariable = num_var, font=('calibre',10,'normal'))
    
    # creating a label for password
    # passw_label = tk.Label(win, text = 'Direction', font = ('calibre',10,'bold'))
    passw_label = OptionMenu( win , way_var , *options )
    
    # creating a entry for password
    passw_entry=tk.Entry(win, textvariable = way_var, font = ('calibre',10,'normal'))
    
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn=tk.Button(win,text = 'Submit', command = submit)
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
    win.mainloop()
    # print(dist, direction)

    countdownTimer()
    startup()
    # grass_encounter(dist, direction)
    # dist = winput("What distance are you running")
    # direction = winput("What direction are you running?")
    # TODO: input from user, up and down, left and right, how many, etc.
    # # gonna need a keyboard interupt
    encounter(dist, direction)

if __name__ == '__main__':
    main()
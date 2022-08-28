from tkinter import *

import os
import tkinter as tk

root = tk.Tk()


root.minsize(height=400,width=300)
root.title(" Pro Kabaddi Database")

Label(root,text="Please fill player information :", font="comicsanms 13 bold",pady=15).grid(row=0,column=3)


def CallBack():
    filename = 'team.py'
    os.system(filename)
    os.system('notepad'+filename)
Label(root,text="Please fill team information :", font="comicsanms 13 bold",pady=15).grid(row=5,column=3)
mybutton2 = Button(root, text=" ADD TEAM" , padx=20,pady=10, fg="red",bg="black",command=CallBack).grid(row=6,column=3)

def CallBack():
    filename = 'player.py'
    os.system(filename)
    os.system('notepad'+filename)

mybutton3 = Button(root, text="ADD PLAYER" , padx=20,pady=10, fg="red",bg="black",command=CallBack).grid(row= 3,column=3) 





root.mainloop()
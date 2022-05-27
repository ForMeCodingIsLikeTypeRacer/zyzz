import tkinter as tk
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import os

root = tk.Tk()
root.attributes('-fullscreen', True)


def donothing():
   x = 0

def summonCat():
    img=PhotoImage(file="zyzz.png")
    panel = Label(canvas, image=img)
    panel.photo = img
    panel.place(x=100,y=150)
    
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
menubar.add_command(label="Exit", command=root.quit)

root.config(menu=menubar)

canvas = tk.Canvas(root,bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

ButtonCat = tk.Button(root,text="Button ZYZZ",padx=1,pady=1,fg="white",bg="#263D42",command=summonCat)
ButtonCat.place(x=100,y=100)


root.mainloop()
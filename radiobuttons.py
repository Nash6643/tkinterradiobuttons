import tkinter as tk
import pygame
import os

root = tk.Tk()


root.title("Suck dick")

root.geometry("400x400")
v = tk.IntVar()
v.set(2)

languages = [("Python",101),
             ("JavaScript",102),
             ("C#",103),
             ("C++",104),
             ]
def ShowChoice():
    print(v.get())

Book = tk.Label(root,text= "Pick your language")
Book.pack()

"""
This is for a boxed type selection
for language, val in languages:
    tk.Radiobutton(root,
                   text=language,
                   indicatoron=0,
                   width=10,
                   padx = 20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)
"""

#This is for a circle type selection
for language, val in languages:
    tk.Radiobutton(root,
                   text=language,
                   padx = 20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)                 
root.mainloop()

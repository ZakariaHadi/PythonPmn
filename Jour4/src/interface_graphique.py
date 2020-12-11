import tkinter
from tkinter import *

root = Tk()  

root.title("Interface graphique")
root.geometry("400x400")
widget_first = Label(root, text="hello zikos !" )

var_entry = tkinter.StringVar()
widget_second = Entry(root, textvariable=var_entry )

widget_first.pack()  
widget_second.pack()  
root.mainloop() 
#!/user/bin/python

##IMPORT MODULES###############################################################
import math
import tkinter as tk
from tkinter import messagebox as mbx
from tkinter import font as tkFont
###############################################################################

history = {}

##FUNCTIONS####################################################################
def sin():
    try:
        s = float(value.get())
        history[f'sin({s})'] = f'{math.sin(math.radians(s))}'
        mbx.showinfo(f'sin({s})=', math.sin(math.radians(s)))
    except ValueError:
        mbx.showerror('Error', """That's not a valid entry.\nPlease enter a number and try again.""")
def cos():
    try:
        s = float(value.get())
        history[f'cos({s})'] = f'{math.cos(math.radians(s))}'
        mbx.showinfo(f'cos({s})=', math.cos(math.radians(s)))
    except ValueError:
        mbx.showerror('Error', "That's not a valid entry.\nPlease enter a number and try again.")
def tan():
    try:
        s = float(value.get())
        history[f'tan({s})'] = f'{math.tan(math.radians(s))}'
        mbx.showinfo(f'tan({s})=', math.tan(math.radians(s)))
    except ValueError:
        mbx.showerror('Error:', "That's not a valid entry.\nPlease enter a number and try again.")
def asin():
    try:
        s = float(value.get())
        if s > 1 or s < -1:
            mbx.showerror('Domain Error:','Please enter a number on [-1,1] and try again.')
        else:
            history[f'asin({s})'] = f'{math.asin(math.radians(s))}'
            mbx.showinfo(f'asin({s})=', math.asin(math.radians(s)))
    except ValueError:
        mbx.showerror('Error', "That's not a valid entry.\nPlease enter a number and try again.")
def acos():
    try:
        s = float(value.get())
        if s > 1 or s < -1:
            mbx.showerror('Domain Error:','Please enter a number on [-1,1] and try again.')
        else:
            history[f'acos({s})'] = f'{math.acos(math.radians(s))}'
            mbx.showinfo(f'acos({s})=', math.acos(math.radians(float(s))))
    except ValueError:
        mbx.showerror('Error', "That's not a valid entry.\nPlease enter a number and try again.")
def atan():
    try:
        s = float(value.get())
        if s > 1 or s < -1:
            mbx.showerror('Domain Error:','Please enter a number on [-1,1] and try again.')
        else:
            history[f'atan({s})'] = f'{math.atan(math.radians(s))}'
            mbx.showinfo(f'atan({s})=', math.atan(math.radians(float(s))))
    except ValueError:
        mbx.showerror('Error', "That's not a valid entry.\nPlease enter a number and try again.")
def ln():
    try:
        s = float(value.get())
        if s < 0:
            mbx.showerror('Domain Error:','Please enter a number > 0 and try again.')
        else:
            history[f'ln({s})'] = f'{math.log(math.radians(s))}'
            mbx.showinfo(f'ln({s})=', math.log(float(s)))
    except ValueError:
        mbx.showerror('Error', "That's not a valid entry.\nPlease enter a number and try again.")
def sqrt():
    try:
        s = float(value.get())
        if s < 0:
            mbx.showerror('Domain Error:','Please enter a number > 0 and try again.')
        else:
            history[f'√({s})'] = f'{math.sqrt(s)}'
            mbx.showinfo(f'√{s}=', math.sqrt(float(s)))
    except ValueError:
        mbx.showerror('Error', "That's not a valid entry.\nPlease enter a number and try again.")
def fact():
    try:
        s = int(value.get())
        history[f'{s}!'] = f'{math.factorial(s)}'
        mbx.showinfo(f'{s}!=', math.factorial(s))
    except ValueError:
        mbx.showerror('Error', "That's not a valid entry.\nPlease enter a positive interger and try again.")
def exit():
    top.destroy()
    print("Thank you for using my program! \nHeres'a list of the opperations you performed:\n")
    for key, value in history.items():
        print(f'{key} = {value}')
###############################################################################

##MAINLOOP#####################################################################
top = tk.Tk()

##INPUT BOX##
value = tk.Entry(top, bd = 5, width = 30)

##BUTTONS##
btnSin = tk.Button(top, text = 'sin(x)', command = sin, padx = 20, bd = 4,
    width = 10, height = 2)
btnCos = tk.Button(top, text = 'cos(x)',   command = cos,  padx = 20, bd = 4,
    width = 10, height = 2)
btnTan = tk.Button(top, text = 'tan(X)',   command = tan,  padx = 20, bd = 4,
    width = 10, height = 2)
btnAsn = tk.Button(top, text = 'asin(x)',  command = asin, padx = 20, bd = 4,
    width = 10, height = 2)
btnAcs = tk.Button(top, text = 'acos(x)',  command = acos, padx = 20, bd = 4,
    width = 10, height = 2)
btnAtn = tk.Button(top, text = 'atan(x)',  command = atan, padx = 20, bd = 4,
    width = 10, height = 2)
btnLn  = tk.Button(top, text = 'ln(x)',    command = ln,   padx = 20, bd = 4,
    width = 10, height = 2)
btnSqt = tk.Button(top, text = '√x',  command = sqrt, padx = 20, bd = 4,
    width = 10, height = 2)
btnFct = tk.Button(top, text = 'x!', command = fact, padx = 20, bd = 4,
    width = 10, height = 2)
btnExt = tk.Button(top, text = 'Exit', command = exit, padx = 20, bd =4,
    width = 10, height = 1)

##BUTTON SPACING##
value.grid (row = 0, column = 0, columnspan = 3)
btnSin.grid(row = 1, column = 0)
btnCos.grid(row = 1, column = 1)
btnTan.grid(row = 1, column = 2)
btnAsn.grid(row = 2, column = 0)
btnAcs.grid(row = 2, column = 1)
btnAtn.grid(row = 2, column = 2)
btnLn.grid (row = 3, column = 0)
btnSqt.grid(row = 3, column = 1)
btnFct.grid(row = 3, column = 2)
btnExt.grid(row = 4, column = 2)

top.mainloop()
###############################################################################

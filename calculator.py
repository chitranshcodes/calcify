from tkinter import *
from PIL import Image, ImageTk
def digit(n):
    var.set(var.get()+n)
def equal():
    var.set(eval(var.get()))

window=Tk()
window.title("Calculator")
window.configure(bg='light blue')
var= StringVar()
window.geometry('300x400')
window.resizable(False,False)
Label(window, text='Calcify',width=20, font="'Times' 16 bold"   ,fg='dark green', bg='yellow').grid(row=0, columnspan=3)
Entry(window, textvariable=var).grid(row=1, columnspan=3)
Button(window, text='7', width=14, command=lambda:digit('7')).grid(row=2,column=0)
Button(window, text='8', width=14, command=lambda:digit('8')).grid(row=2,column=1)
Button(window, text='9', width=14, command=lambda:digit('9')).grid(row=2,column=2)
Button(window, text='4', width=14, command=lambda:digit('4')).grid(row=3,column=0)
Button(window, text='5', width=14, command=lambda:digit('5')).grid(row=3,column=1)
Button(window, text='6', width=14, command=lambda:digit('6')).grid(row=3,column=2)
Button(window, text='3', width=14, command=lambda:digit('3')).grid(row=4,column=0)
Button(window, text='2', width=14, command=lambda:digit('2')).grid(row=4,column=1)
Button(window, text='1', width=14, command=lambda:digit('1')).grid(row=4,column=2)
Button(window, text='+', width=14, command=lambda:digit('+')).grid(row=5,column=0)
Button(window, text='0', width=14, command=lambda:digit('0')).grid(row=5,column=1)
Button(window, text='-', width=14, command=lambda:digit('-')).grid(row=5,column=2)
Button(window, text='x', width=14, command=lambda:digit('*')).grid(row=6,column=0)
Button(window, text='=', width=14, command=equal).grid(row=6,column=1)
Button(window, text='/', width=14, command=lambda:digit('7')).grid(row=6,column=2)
Button(window, text='clear', width=14, command=lambda:var.set("")).grid(row=7,column=1)
img = Image.open(r"C:/Users/CHITRANSH GAUR/OneDrive/Desktop/Projects/tkinter-calci/calcify/hiladala.png")
img = img.resize((280, 200))
img = ImageTk.PhotoImage(img)

Label(window, image=img).grid(row=8,columnspan=3, padx=0)


window.mainloop()

import tkinter
from tkinter import *
import pyperclip
import random
win=Tk()
win.title('Random Password Generator')
win.geometry('450x450')
win.iconbitmap('pass.ico')
passstr=StringVar()
passlen=IntVar()
passlen.set(0)
def generate():
    pass1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','','!','@','#','$','%','^','&','*','//']
    password=""
    for x in range(passlen.get()):
        password=password+random.choice(pass1)
    passstr.set(password)
def copytoclipboard():
    random_password=passstr.get()
    pyperclip.copy(random_password)
Label(win,text="Password Generator Application",font="Calibri 20 bold").pack()
Label(win,text="Enter Password Length").pack(pady=3)
Entry(win,textvariable=passlen).pack(pady=3)
Button(win,text="Generate Password",command=generate).pack()
Entry(win,textvariable=passstr).pack(pady=3)
Button(win,text="Copy to Clipboard",command=copytoclipboard).pack()
win.mainloop()


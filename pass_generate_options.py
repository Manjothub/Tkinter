import tkinter
from tkinter import *
import random
win=Tk()
win.geometry("500x300")
win.title('Password Generator')
win.iconbitmap('pass.ico')
chk1=IntVar()
chk2=IntVar()
chk3=IntVar()
passenter=IntVar()
def password_generate(len):
    valid_char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password="".join(random.sample(valid_char,len))
    disp_result.delete(0,END)
    disp_result.insert(0,password)
def checkbox_check():
    if chk1.get()==6:
        password_generate(6)
    elif chk2.get()==10:
        password_generate(10)
    elif chk3.get()==12:
        password_generate(12)
    else:
        password_generate(passenter.get())
    
disp_text=Label(win,text='Password Generator Bro',font=('Arial',20)).pack()
disp_result=Entry()
disp_result.pack()
chkbtn1=Checkbutton(win,text='6 Character',onvalue=6,offvalue=0,variable=chk1).pack()
chkbtn2=Checkbutton(win,text='10 Character',onvalue=10,offvalue=0,variable=chk2).pack()
chkbtn3=Checkbutton(win,text='12 Character',onvalue=12,offvalue=0,variable=chk3).pack()
lb=Label(win,text='Enter Your Choice').pack()
show=Entry(win,textvariable=passenter).pack()
submit=Button(win,text='Generate',command=checkbox_check).pack()
win.mainloop()
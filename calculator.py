import tkinter
from tkinter import *
win=Tk()
win.geometry("320x320")
win.title('Calculator')


#function Coding Starts Here
exp=""
equation=StringVar()
def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)

def clear():
    global exp
    exp=""
    equation.set("")
def equal():
    global exp
    u=eval(exp)
    equation.set(u)
    exp=str(u)
    
def equal():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp=""
    except:
        equation.set("error")
        exp=""


write_pad=Entry(win,justify='right',textvariable=equation,font=('Arial',20)).grid(rowspan=1,columnspan=100,ipadx=10,ipady=20)
btn_num7=Button(win,text=7,command=lambda:press(7)).grid(row=2,column=0,ipadx=32  ,ipady=10)
btn_num8=Button(win,text=8,command=lambda:press(8)).grid(row=2,column=1,ipadx=32,ipady=10)
btn_num9=Button(win,text=9,command=lambda:press(9)).grid(row=2,column=2,ipadx=32,ipady=10)
btn_numx=Button(win,text="x",command=lambda:press('*')).grid(row=2,column=3,ipadx=32,ipady=10)

#Next Row Started
btn_num4=Button(win,text=4,command=lambda:press(4)).grid(row=3,column=0,ipadx=32  ,ipady=10)
btn_num5=Button(win,text=5,command=lambda:press(5)).grid(row=3,column=1,ipadx=32,ipady=10)
btn_num6=Button(win,text=6,command=lambda:press(6)).grid(row=3,column=2,ipadx=32,ipady=10)
btn_num_add=Button(win,text="+",command=lambda:press('+')).grid(row=3,column=3,ipadx=32,ipady=10)

#Next Row Started
btn_num1=Button(win,text=1,command=lambda:press(1)).grid(row=4,column=0,ipadx=32  ,ipady=10)
btn_num2=Button(win,text=2,command=lambda:press(2)).grid(row=4,column=1,ipadx=32,ipady=10)
btn_num3=Button(win,text=3,command=lambda:press(3)).grid(row=4,column=2,ipadx=32,ipady=10)
btn_num_sub=Button(win,text="-",command=lambda:press('-')).grid(row=4,column=3,ipadx=32,ipady=10)

#Next Row Started
btn_num0=Button(win,text=0,command=lambda:press(0)).grid(row=5,column=0,ipadx=32  ,ipady=10)
btn_num=Button(win,text='.',command=lambda:press('.')).grid(row=5,column=1,ipadx=32,ipady=10)
btn_num_equal=Button(win,text='=',command=equal).grid(row=5,column=2,ipadx=32,ipady=10)
btn_num_dvd=Button(win,text="/",command=lambda:press('/')).grid(row=5,column=3,ipadx=32,ipady=10)

#lastbutton
btn_num_clear=Button(win,text='C',command=clear).grid(rowspan=6,columnspan=100,ipadx=150,ipady=20)


win.mainloop()
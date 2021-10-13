import tkinter
from tkinter import *
from tkinter import messagebox
win=Tk()
win.geometry("400x250")


# redbutton=Button(win,text="Red",fg="red")
# redbutton.pack(side=LEFT)
# bluebutton=Button(win,text="Blue",fg="Blue")
# bluebutton.pack(side=RIGHT)
# greenbutton=Button(win,text="Green",fg="Green")
# greenbutton.pack(side=TOP)
# yellowbutton=Button(win,text="Yellow",fg="Yellow")
# yellowbutton.pack(side=BOTTOM)
# name=Label(win,text="UserName").grid(row=0,column=0)
# e1=Entry(win).grid(row=0,column=1)
# password=Label(win,text="Password").grid(row=1,column=0)
# e2=Entry(win).grid(row=1,column=1)
# submit=Button(win,text="Submit").grid(row=4,column=0)




# win.geometry("400x250")
# name=Label(win,text="Username").place(x=30,y=50)
# email=Label(win,text="Email").place(x=30,y=90) 
# password=Label(win,text="Password").place(x=30,y=130)
# e1=Entry(win).place(x=80,y=50)
# e2=Entry(win).place(x=80,y=90)
# e3=Entry(win).place(x=95,y=130)
# submit=Button(win,text="Submit").place(x=30,y=150)

def fun():
    messagebox.showinfo("Hello","Button Clicked")
b1=Button(win,text="Red",command=fun,activeforeground="red",activebackground="pink",pady=10)
b2=Button(win,text="Blue",command=fun,activeforeground="Blue",activebackground="pink",pady=10)
b3=Button(win,text="Green",command=fun,activeforeground="Green",activebackground="pink",pady=10)
b4=Button(win,text="Yellow",command=fun,activeforeground="Yellow",activebackground="pink",pady=10)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)
win.mainloop()
# def fun():  
#     messagebox.showinfo("Hello", "Red Button clicked")  
  
  
# b1 = Button(top,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  
  
# b2 = Button(top, text = "Blue",activeforeground = "blue",activebackground = "pink",pady=10)  
  
# b3 = Button(top, text = "Green",activeforeground = "green",activebackground = "pink",pady = 10)  
  
# b4 = Button(top, text = "Yellow",activeforeground = "yellow",activebackground = "pink",pady = 10)  
  
# b1.pack(side = LEFT)  
  
# b2.pack(side = RIGHT)  
  
# b3.pack(side = TOP)  
  
# b4.pack(side = BOTTOM)  
  
# top.mainloop()  


import tkinter
from tkinter import *
from tkinter import ttk

exp=" "
def press(num):
    global exp
    exp+=str(num)
    eq.set(exp)
def clear():
    global exp
    exp=" "
    eq.set(exp)
def action():
    global exp
    exp="Next Line:"
    eq.set(exp)
    
win=Tk()
win.title('on-screen keyboard')
win.geometry('1010x250')
win.maxsize(width=1400,height=250)
win.minsize(width=1400, height=250)
win.iconbitmap('key.ico')
#function Coding

eq=StringVar()
display_entry=ttk.Entry(win,state='readonly',textvariable=eq)
display_entry.grid(rowspan=1,columnspan=100,ipadx=999,ipady=20)
win.configure(bg='black')    #for color printing
q=ttk.Button(win,text='Q',command=lambda:press('Q'))
q.grid(row=1,column=0,ipadx=6,ipady=10)

w=ttk.Button(win,text='W',command=lambda:press('W'))
w.grid(row=1,column=1,ipadx=6,ipady=10)

e=ttk.Button(win,text='E',command=lambda:press('E'))
e.grid(row=1,column=2,ipadx=6,ipady=10)

r=ttk.Button(win,text='R',command=lambda:press('R'))
r.grid(row=1,column=3,ipadx=6,ipady=10)

t=ttk.Button(win,text='T',command=lambda:press('T'))
t.grid(row=1,column=4,ipadx=6,ipady=10)

y=ttk.Button(win,text='Y',command=lambda:press('Y'))
y.grid(row=1,column=5,ipadx=6,ipady=10)

u=ttk.Button(win,text='U',command=lambda:press('U'))
u.grid(row=1,column=6,ipadx=6,ipady=10)

i=ttk.Button(win,text='I',command=lambda:press('I'))
i.grid(row=1,column=7,ipadx=6,ipady=10)

o=ttk.Button(win,text='O',command=lambda:press('O'))
o.grid(row=1,column=8,ipadx=6,ipady=10)

p=ttk.Button(win,text='P',command=lambda:press('P'))
p.grid(row=1,column=9,ipadx=6,ipady=10)

cur_c=ttk.Button(win,text='{',command=lambda:press('{'))
cur_c.grid(row=1,column=10,ipadx=6,ipady=10)

cur=ttk.Button(win,text='}',command=lambda:press('}'))
cur.grid(row=1,column=11,ipadx=6,ipady=10)

bckslsh=ttk.Button(win,text='\\',command=lambda:press('\\'))
bckslsh.grid(row=1,column=12,ipadx=6,ipady=10)

clear=ttk.Button(win,text='Backspace',command=clear)
clear.grid(row=1,column=13,ipadx=6,ipady=10)


#next row
a=ttk.Button(win,text='A',command=lambda:press('A'))
a.grid(row=2,column=0,ipadx=6,ipady=10)

s=ttk.Button(win,text='S',command=lambda:press('S'))
s.grid(row=2,column=1,ipadx=6,ipady=10)

d=ttk.Button(win,text='D',command=lambda:press('D'))
d.grid(row=2,column=2,ipadx=6,ipady=10)

f=ttk.Button(win,text='F',command=lambda:press('F'))
f.grid(row=2,column=3,ipadx=6,ipady=10)

g=ttk.Button(win,text='G',command=lambda:press('G'))
g.grid(row=2,column=4,ipadx=6,ipady=10)

h=ttk.Button(win,text='H',command=lambda:press('H'))
h.grid(row=2,column=5,ipadx=6,ipady=10)

j=ttk.Button(win,text='J',command=lambda:press('J'))
j.grid(row=2,column=6,ipadx=6,ipady=10)

k=ttk.Button(win,text='K',command=lambda:press('K'))
k.grid(row=2,column=7,ipadx=6,ipady=10)

l=ttk.Button(win,text='L',command=lambda:press('L'))
l.grid(row=2,column=8,ipadx=6,ipady=10)

cur_dot=ttk.Button(win,text=':',command=lambda:press(':'))
cur_dot.grid(row=2,column=9,ipadx=6,ipady=10)

cur_comma=ttk.Button(win,text=' " ',command=lambda:press('"'))
cur_comma.grid(row=2,column=10,ipadx=6,ipady=10)

enter=ttk.Button(win,text='Enter',width=6,command=action)
enter.grid(row=2,column=11,columnspan=5,ipadx=107,ipady=10)


win.mainloop()
from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('Counter Program')
GUI.geometry('500x300')

######progress#######
progress = ttk.Progressbar(GUI,orient="horizontal",length=450, mode="determinate")
progress.place(x=20,y=50)
progress['maximum'] = 10


L = ttk.Label(GUI,text='จำนวนคนทั้งหมด')
L.grid(row=0,column=0,padx=10)

v_total = IntVar()
v_total.set(10)

E1 = ttk.Entry(GUI,textvariable=v_total,font=(None,20),width=5)
E1.grid(row=0,column=1,padx=10)

current_total = 10
def settotal():
    global progress_value
    progress_value = 0
    global current_total
    current_total = v_total.get()
    print(current_total)
    progress['maximum'] = current_total
    progress['value'] = 0
    text = '{}/{}'.format(progress_value,v_total.get())
    v_result.set(text)

B1 = ttk.Button(GUI,text='Save / Reset',command=settotal)
B1.grid(row=0,column=2,padx=10)

FB = Frame()
FB.place(x=50,y=100)

progress_value = 0

def Plus():
    global progress_value
    progress_value += 1
    progress['value'] = progress_value
    text = '{}/{}'.format(progress_value,v_total.get())
    v_result.set(text)

def Minus():
    global progress_value
    progress_value -= 1
    progress['value'] = progress_value
    text = '{}/{}'.format(progress_value,v_total.get())
    v_result.set(text)


B2 = ttk.Button(FB,text='+',command=Plus)
B2.grid(row=0,column=1,padx=10,ipadx=30,ipady=20)

B3 = ttk.Button(FB,text='-',command=Minus)
B3.grid(row=0,column=2,padx=10,ipadx=30,ipady=20)

v_result = StringVar()
v_result.set('0/10')

result = ttk.Label(GUI,textvariable=v_result,font=(None,40))
result.place(x=100,y=200)


GUI.mainloop()

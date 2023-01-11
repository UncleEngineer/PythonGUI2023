# first-gui.py

from tkinter import *

GUI = Tk() # โปรแกรมหลัก
GUI.title('โปรแกรมแรกของลุง') # ชื่อโปรแกรม
GUI.geometry('1000x300')

L = Label(GUI,text='Python GUI 2023',font=('Angsana New',100,'bold'))
# L.pack()
L.place(x=150,y=20)

GUI.mainloop()

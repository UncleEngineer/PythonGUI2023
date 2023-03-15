from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x400')


CV = Canvas(GUI,width=500,height=500)
CV.place(x=0,y=50)

def Barchart(height=200,data=[400,200,300],color=['red','green','blue'],gwidth=50):
    diff = 5
    maxdata = max(data)
    for i,(d,c) in enumerate(zip(data,color)):
        v = (d/maxdata) * 100 * (height/100)
        y = (height - v) + diff
        g1 = CV.create_rectangle( (gwidth * i) + 10,y,(gwidth * (i+1)), height ,fill=c) 
    # value1 = (data[0] / maxdata) * 100 * (height/100)
    # value2 = (data[1] / maxdata) * 100 * (height/100)
    # value3 = (data[2] / maxdata) * 100 * (height/100)
    
    # y1 = (height - value1) + diff
    # y2 = (height - value2)  + diff
    # y3 = (height - value3)  + diff


    # g1 = CV.create_rectangle((gwidth * 0) + 10,y1,(gwidth * 1), height ,fill='red')
    # g2 = CV.create_rectangle((gwidth * 1) + 10,y2,(gwidth * 2), height ,fill='green')
    # g3 = CV.create_rectangle((gwidth * 2) + 10,y3,(gwidth * 3), height ,fill='blue')

Barchart(data=[444,256,310,600,100],color=['red','green','blue','pink','purple'])

GUI.mainloop()
from tkinter import *
from tkinter import ttk # theme of Tk

GUI = Tk()
GUI.geometry('700x500')
GUI.title('โปรแกรมหารกัน')

L = Label(GUI,text='โปรแกรมหารกัน',font=('Angsana New',30))
L.pack(pady=20)

##############E1###############
L = Label(GUI,text='ราคาอาหารทั้งหมด (บาท)',font=('Angsana New',20))
L.pack(pady=5)

v_total = StringVar() #StringVar ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(GUI,textvariable=v_total ,font=('Angsana New',20))
E1.pack(pady=10)

##############E2###############
L = Label(GUI,text='มากันกี่คน?',font=('Angsana New',20))
L.pack(pady=5)

v_person = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_person,font=('Angsana New',20))
E2.pack(pady=10)
##############BUTTON###############
def Calculate():
    total = float(v_total.get())
    person = int(v_person.get())
    calc = total / person
    print('Split (baht/person): ',calc)
    # รวมทั้งหมด 3,000 บาท (600 บาทต่อคน) 
    text = 'รวมทั้งหมด {:,.2f} บาท จำนวน {} คน ({:.2f} บาทต่อคน)'.format(total,person,calc)
    v_result.set(text)
    # from tkinter import messagebox
    # messagebox.showinfo('หารกันคนละ...',text)

B1 = ttk.Button(GUI,text='Calculate', command=Calculate)
B1.pack(pady=10,ipadx=20,ipady=10)

v_result = StringVar()
result = ttk.Label(GUI,textvariable=v_result,font=('Angsana New',30,'bold'),foreground='green')
result.pack(pady=10)

# def Close():
#     GUI.quit()

# F1 = Frame(GUI)
# F1.place(x=50,y=50)
# B2 = ttk.Button(F1,text='X',width=5,command=Close)
# B2.pack(ipadx=20)
GUI.mainloop()
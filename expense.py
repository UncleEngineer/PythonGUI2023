from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime
#######################
import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# EXPENSE
c.execute("""CREATE TABLE IF NOT EXISTS expense (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            date TEXT)""")

# INCOME
c.execute("""CREATE TABLE IF NOT EXISTS income (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            date TEXT)""")

#########EXPENSE#########
def insert_expense(title,price,date):
    with conn:
        command = 'INSERT INTO expense VALUES (?,?,?,?)'
        c.execute(command, (None,title,price,date))
    conn.commit() # บันทึกข้อมูลเหมือนกับเซฟไฟล์
    print('saved')



def view_all_expense():
    with conn:
        command = 'SELECT * FROM expense'
        c.execute(command)
        result = c.fetchall()
        #print(result)
    return result

def update_expense(ID,field,newvalue):
    with conn:
        command = 'UPDATE expense SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(command, ([newvalue,ID]))
    conn.commit()
    print('updated')


def delete_expense(ID):
    with conn:
        command = 'DELETE FROM expense WHERE ID=(?)'
        c.execute(command,([ID]))
    conn.commit()
    print('deleted')


#########INCOME#########
def insert_income(title,price,date):
    with conn:
        command = 'INSERT INTO income VALUES (?,?,?,?)'
        c.execute(command, (None,title,price,date))
    conn.commit() # บันทึกข้อมูลเหมือนกับเซฟไฟล์
    print('saved')



def view_all_income():
    with conn:
        command = 'SELECT * FROM income'
        c.execute(command)
        result = c.fetchall()
        #print(result)
    return result

def update_income(ID,field,newvalue):
    with conn:
        command = 'UPDATE income SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(command, ([newvalue,ID]))
    conn.commit()
    print('updated')


def delete_income(ID):
    with conn:
        command = 'DELETE FROM income WHERE ID=(?)'
        c.execute(command,([ID]))
    conn.commit()
    print('deleted')

#######################
def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

def readcsv():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = list(csv.reader(file))
        #print(fr)
    return fr


GUI = Tk()
GUI.geometry('800x700')
GUI.state('zoomed')
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')

FONT1 = ('Angsana New',25)

#################### Config TAB 1##################
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')
icon_tab3 = PhotoImage(file='tab3.png')

Tab.add(T1,text='บันทึกค่าใช้จ่าย',image=icon_tab1,compound='left')
Tab.add(T2,text='บันทึกรายรับ',image=icon_tab2,compound='left')
Tab.add(T3,text='ประวัติค่าใช้จ่าย',image=icon_tab3,compound='left')
#######################TAB 1#######################

FT1 = Frame(T1)
FT1.place(x=50,y=50)

# IMAGE
icon = 'C:\\Users\\Uncle Engineer\\Desktop\\Python GUI 2023\\expense.png'
iconimage = PhotoImage(file=icon)
L = Label(FT1,image=iconimage)
L.pack()

# ช่องรายการค่าใช้จ่าย
L = Label(FT1,text='รายการค่าใช้จ่าย', font=(None,30))
L.pack(pady=5)

v_expense = StringVar()
E1 = ttk.Entry(FT1, textvariable=v_expense, font=FONT1)
E1.pack(pady=5)

# ช่องกรอกจำนวนเงินค่าใช้จ่าย
L = Label(FT1,text='จำนวนเงิน (บาท)', font=(None,30))
L.pack(pady=5)

v_amount = StringVar()
E2 = ttk.Entry(FT1, textvariable=v_amount, font=FONT1)
E2.pack(pady=5)

# ปุ่มบันทึกข้อมูล

def update_table():
    #   Clear Table
    table.delete(*table.get_children())
    data = view_all_expense()
    for d in data:
        table.insert('','end',values=[d[0],d[1],d[2],d[3]])


def SaveData(event=None):
    expense = v_expense.get()
    amount = float(v_amount.get())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # data = [expense, amount, timestamp]
    # writecsv(data)

    insert_expense(expense,amount,timestamp)
    v_expense.set('')
    v_amount.set('')
    E1.focus()
    update_table()

E2.bind('<Return>',SaveData) # event=None
E1.bind('<Return>', lambda x: E2.focus()) #ฟังชั่นพิเศษ bind โดยไม่ต้องสร้างฟังชั่น


def Fav1(event=None):
    v_expense.set('น้ำเต้าหู้')
    v_amount.set('15')


GUI.bind('<F1>',Fav1)


B1 = ttk.Button(FT1,text='บันทึก',command=SaveData)
B1.pack(ipadx=20,ipady=10,pady=5)


#######TABLE - EXPENSE######

# น้ำเต้าหู้,50.0,2023-01-11 21:12:43
header = ['ID','รายการ','ค่าใช้จ่าย','วัน-เวลา']
hwidth = [70,300,150,170]

table = ttk.Treeview(T1, columns=header, show='headings', height=20)
table.place(x=400,y=50)

# resize
style = ttk.Style()
style.configure('Treeview.Heading',font=(None,15))
style.configure('Treeview',font=(None,13),rowheight=30)

# table.column('ลำดับ',width=50)
# table.heading('ลำดับ',text='ลำดับ')

table.column('ค่าใช้จ่าย',anchor=E)
table.column('รายการ',anchor=CENTER)

for h,w in zip(header,hwidth):
    table.column(h,width=w)
    table.heading(h,text=h)

# table.insert('','end',values=['A','B','C','D'])
#data = readcsv()

data = view_all_expense()

for i,d in enumerate(data,start=1):
    #d.insert(0,i)
    #table.insert('','end',values=d)
    table.insert('','end',values=[d[0],d[1],d[2],d[3]])

# delete
def delete_data(event):
    select = table.selection() #เช็คว่ามีการเลือกบรรทัดไหน?
    print(select)
    select_data = table.item(select)
    print(select_data['values'][0])
    ID = select_data['values'][0]

    check = messagebox.askyesno('คอนเฟิร์มการลบ','คุณต้องการลบข้อมูลใช่หรือไม่? หากลบแล้วไม่สามารถกู้คืนได้!')
    print([check],type(check))
    if check:
        delete_expense(ID)
        update_table()

def update_data(event):
    select = table.selection()
    select_data = table.item(select)
    ID = select_data['values'][0]
    title = select_data['values'][1]
    price = select_data['values'][2]

    GUI2 = Toplevel()
    GUI2.geometry('500x400')
    GUI2.title('แก้ไขรายการ')

    L = Label(GUI2,text='รายการค่าใช้จ่าย', font=(None,30))
    L.pack(pady=5)

    v_expense2 = StringVar()
    v_expense2.set(title)
    E1 = ttk.Entry(GUI2, textvariable=v_expense2, font=FONT1)
    E1.pack(pady=5)

    
    L = Label(GUI2,text='จำนวนเงิน (บาท)', font=(None,30))
    L.pack(pady=5)

    v_amount2 = StringVar()
    v_amount2.set(price)
    E2 = ttk.Entry(GUI2, textvariable=v_amount2, font=FONT1)
    E2.pack(pady=5)

    def UpdateData():
        update_expense(ID,'title',v_expense2.get())
        update_expense(ID,'price',float(v_amount2.get()))
        update_table()
        GUI2.destroy() #ปิดหน้าต่าง GUI2 ทิ้ง อยากใช้ค่อยเปิดใหม่

    B1 = ttk.Button(GUI2,text='บันทึก',command=UpdateData)
    B1.pack(ipadx=20,ipady=10,pady=5)

    GUI2.mainloop()

table.bind('<Double-1>',update_data)
table.bind('<Delete>',delete_data) # don't forget 'event' in function

#######################TAB 2#######################

FT2 = Frame(T2)
FT2.place(x=50,y=50)
# ช่องรายการรายรับ
L = Label(FT2,text='รายการรายรับ', font=(None,30))
L.pack(pady=5)

v_income = StringVar()
E21 = ttk.Entry(FT2, textvariable=v_income, font=FONT1)
E21.pack(pady=5)

# ช่องกรอกจำนวนเงินรายรับ
L = Label(FT2,text='จำนวนเงิน (บาท)', font=(None,30))
L.pack(pady=5)

v_amount2 = StringVar()
E22 = ttk.Entry(FT2, textvariable=v_amount2, font=FONT1)
E22.pack(pady=5)

def update_table2():
    #   Clear Table
    table2.delete(*table2.get_children())
    data = view_all_income()
    for d in data:
        table2.insert('','end',values=[d[0],d[1],d[2],d[3]])

def SaveIncome(event=None):
    income = v_income.get()
    amount = float(v_amount2.get())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # data = [expense, amount, timestamp]
    # writecsv(data)

    insert_income(income,amount,timestamp)
    v_income.set('')
    v_amount2.set('')
    E21.focus()
    update_table2()


B2 = ttk.Button(FT2,text='บันทึก',command=SaveIncome)
B2.pack(ipadx=20,ipady=10,pady=5)

E22.bind('<Return>',SaveIncome) # event=None
E21.bind('<Return>', lambda x: E22.focus()) #ฟังชั่นพิเศษ bind โดยไม่ต้องสร้างฟังชั่น

#######TABLE - INCOME######

# น้ำเต้าหู้,50.0,2023-01-11 21:12:43
header = ['ID','รายการ','รายรับ','วัน-เวลา']
hwidth = [70,300,150,170]

table2 = ttk.Treeview(T2, columns=header, show='headings', height=20)
table2.place(x=400,y=50)

# resize
style = ttk.Style()
style.configure('Treeview.Heading',font=(None,15))
style.configure('Treeview',font=(None,13),rowheight=30)

# table.column('ลำดับ',width=50)
# table.heading('ลำดับ',text='ลำดับ')

table2.column('รายรับ',anchor=E)
table2.column('รายการ',anchor=CENTER)

for h,w in zip(header,hwidth):
    table2.column(h,width=w)
    table2.heading(h,text=h)

# table.insert('','end',values=['A','B','C','D'])
#data = readcsv()

data = view_all_income()

for i,d in enumerate(data,start=1):
    #d.insert(0,i)
    #table.insert('','end',values=d)
    table2.insert('','end',values=[d[0],d[1],d[2],d[3]])

# delete
def delete_data2(event):
    select = table2.selection() #เช็คว่ามีการเลือกบรรทัดไหน?
    print(select)
    select_data = table2.item(select)
    print(select_data['values'][0])
    ID = select_data['values'][0]

    check = messagebox.askyesno('คอนเฟิร์มการลบ','คุณต้องการลบข้อมูลใช่หรือไม่? หากลบแล้วไม่สามารถกู้คืนได้!')
    print([check],type(check))
    if check:
        delete_income(ID)
        update_table2()

def update_data2(event):
    select = table2.selection()
    select_data = table2.item(select)
    ID = select_data['values'][0]
    title = select_data['values'][1]
    price = select_data['values'][2]

    GUI2 = Toplevel()
    GUI2.geometry('500x400')
    GUI2.title('แก้ไขรายการ')

    L = Label(GUI2,text='รายการรายรับ', font=(None,30))
    L.pack(pady=5)

    v_income2 = StringVar()
    v_income2.set(title)
    E21E = ttk.Entry(GUI2, textvariable=v_income2, font=FONT1)
    E21E.pack(pady=5)

    
    L = Label(GUI2,text='จำนวนเงิน (บาท)', font=(None,30))
    L.pack(pady=5)

    v_amount2E = StringVar()
    v_amount2E.set(price)
    E22E = ttk.Entry(GUI2, textvariable=v_amount2E, font=FONT1)
    E22E.pack(pady=5)

    def UpdateData():
        update_income(ID,'title',v_income2.get())
        update_income(ID,'price',float(v_amount2E.get()))
        update_table2()
        GUI2.destroy() #ปิดหน้าต่าง GUI2 ทิ้ง อยากใช้ค่อยเปิดใหม่

    B1 = ttk.Button(GUI2,text='บันทึก',command=UpdateData)
    B1.pack(ipadx=20,ipady=10,pady=5)

    GUI2.mainloop()

table2.bind('<Double-1>',update_data2)
table2.bind('<Delete>',delete_data2) # don't forget 'event' in function


#######################TAB 3#######################



GUI.mainloop()

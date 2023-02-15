import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS expense (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            date TEXT)""")

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

insert_expense('แปรงสีฟัน',60,'2023-02-15 20:50')
#insert_expense('แชมพูตรานางฟ้า',30,'2023-02-15 20:50')
#update_expense(1,'title','สบู่ดอกบัวคู่')
#update_expense(1,'price',50)
#delete_expense(4)
#delete_expense(5)

data = view_all_expense()
print(data)
#print(data[0][1],data[0][2])



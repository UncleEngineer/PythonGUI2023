import csv

def readcsv():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = list(csv.reader(file))
        #print(fr)
    return fr

data = readcsv()
print(data)
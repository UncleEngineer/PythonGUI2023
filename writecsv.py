# writecsv.py

import csv

def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


writecsv(['Apple',20,'2023'])
import csv

data = []
with open('股票代碼對照表.csv',newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        data.append((row[0],row[1]))
data.pop(0)
data.pop(-1)
print(data)

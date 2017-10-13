import csv

with open("C:\DSavilov\Temp\Crimes.csv") as f:
    reader = csv.reader(f)
#    print(len(list(reader)))
    res = {}
    for row in reader:
       if row[5] not in res:
           res[row[5]] = 1
       else:
           res[row[5]] = res[row[5]] + 1


    for drow in res:
        print(drow, res[drow])


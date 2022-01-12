import csv
import string
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'newActivityKuDataSet.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)


    dictDate = {}  # stores number of steps per day
    dictInterval = {}  # stores number of steps per 5 min interval

    listDate = []
    listTotal = []

    for row in reader:
        steps = row[0]
        date = row[1]
        interval = int(row[2])

        dictDate.setdefault(str(date), [])
        dictDate[str(date)].append(int(steps))

        dictInterval.setdefault(interval, [])
        dictInterval[interval].append(int(steps))

    listDate = []
    listTotal = []

    for i in dictDate.keys():
        listDate.append(i)
        listTotal.append(sum(dictDate.get(i)))

    dates = []
    for i in range(len(listDate)):
        dates.append(listDate[i].split("-"))

    for i in range(len(dates)):
        d = datetime(int(dates[i][0]),int(dates[i][1]),int(dates[i][2]))
        if d.weekday() > 4:
            dates[i].append("Weekend")
        else:
            dates[i].append("Weekday")
        print(dates[i])

    wr = open("ActivityWeekday.csv", "w")
    wr.write(str(headerRow[0]) + "," + str(headerRow[1]) + "," + str(headerRow[2]) + "," + "Weekday/Weekend")
    wr.write("\n")
    n = 0
    for row in reader:
        wr.write(str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(dates[n][3]))
        wr.write("\n")
        n += 1

    wr.close()


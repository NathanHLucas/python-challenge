# PyBank text file
import csv
from statistics import mean
import numpy as np

#import csv file information into Python data types
dateList = []
profitList = []


with open("budget_data.csv", "r") as file:
    csvFile = csv.reader(file)

    for row in csvFile:
        dateList.append(row[0])
        profitList.append(row[1])

#clean up data
dateList.remove(dateList[0])
profitList.remove(profitList[0])

#perform calculations

totalMonths = len(dateList)
total = sum(int(x) for x in profitList)

diffList = []
for counter in range(len(profitList)-1):
    diffList.append(int(profitList[counter+1]) - int(profitList[counter]))

print(len(profitList))
print(len(diffList))
print(diffList)

decrease = min(diffList)
dateDecrease = dateList[diffList.index(decrease)+1]
increase = max(diffList)
dateIncrease = dateList[diffList.index(increase)+1]

#generate final report
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${total}")
print(f"Average Change: ${round(mean(int(x) for x in diffList),2)}")
print(f"Greatest Increase in Profits: {dateIncrease} (${increase})")
print(f"Greatest Decrease in Profits: {dateDecrease} (${decrease})")







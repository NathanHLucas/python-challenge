#PyPoll text file

import csv

#import csv file information into Python data types
idList = []
county = []
candidate = []

with open("election_data.csv", "r") as file:
    csvFile = csv.reader(file)

    for row in csvFile:
        idList.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

idList.remove(idList[0])
county.remove(county[0])
candidate.remove(candidate[0])

#perform calculations
totalVotes = len(idList)
candidateList = list(set(candidate))
countList = []
for name in candidateList:
    countList.append(candidate.count(name))

winner = candidateList[countList.index(max(countList))]


#create report
print("Election Results")
print("---------------------------")
print(f"Total Votes: {totalVotes}")
print("---------------------------")
for x in range(len(candidateList)):
    print(f"{candidateList[x]}: {round((countList[x]/totalVotes)*100,3)}% ({countList[x]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


#create text file with final report
with open('solution.txt', 'w') as solFile:
    solFile.write("Election Results\n")
    solFile.write("---------------------------\n")
    solFile.write(f"Total Votes: {totalVotes}\n")
    solFile.write("---------------------------\n")

    for x in range(len(candidateList)):
        solFile.write(f"{candidateList[x]}: {round((countList[x]/totalVotes)*100,3)}% ({countList[x]})\n")
    solFile.write("---------------------------\n")
    solFile.write(f"Winner: {winner}")
    solFile.write("---------------------------\n")

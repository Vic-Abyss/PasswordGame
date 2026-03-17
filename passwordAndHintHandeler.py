# rewrite of Vic-Abyss's work on the getPassword module

#Authors:
    # Nicole Bromberek (Raven System)

# imports
import csv
import random

# class variables
passwordFile = "passwords.csv"
secretRow = []
pastRowNums = []

def getNextSecretRow():
    with open (passwordFile, newline='\r\n') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        rows = []
        for row in reader:
            rows.append(row)
        flag = True
        index = 0
        while flag:
            flag = False
            index = random.randrange(0,len(rows))
            if pastRowNums.__contains__(index):
                flag = True
        secretRow = rows[index]
        pastRowNums.append(index)
        print(secretRow)

# TESTING to validated outputs
# getNextSecretRow()
# getNextSecretRow()
# getNextSecretRow()


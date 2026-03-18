#Password Game Group 3

#Owen, Ylli, and Valerie
import csv
import random
from pathlib import Path
#function to generate a password

# def generatePassword():
#     filename = 'passwordList.txt'
#     all_passwords = []
#     #open file that contains the passwords
#     with open (filename,'r', newline='') as f:
#         reader = csv.reader(f)
#         #read the file contents into a list
#         for row in reader:
#             all_passwords.extend(row)
#     print(all_passwords)

#     #get a random index from the list
#     passwordIndex = random.randrange(len(all_passwords))
#     #variable to hold the choice from the list
#     machinePassword = all_passwords[passwordIndex]
#     print(machinePassword)

#function for taking input
def enterGuess(machinePassword):
    userGuess = input("Enter your password guess: ")
    
    # sanatize user input in future versions

    #call the comparison function
    comparePassword(userGuess, machinePassword)

#function for comparing inputs
def comparePassword(userGuess, machinePassword):
    while machinePassword != userGuess:
        #call the hint function
        hint(passwordIndex)
        input("Enter your new password guess: ")

# if __name__ == '__main__':
#     generatePassword()

    
class passwordAndHintHandeler:
    # rewrite of Vic-Abyss's work on the getPassword method

    #Authors:
        # Nicole Bromberek (Raven System)

    # imports
    # import csv
    # import random
    # from pathlib import Path

    # class variables
        # set this to the selected password file
    passwordFile = ""
        # this is the most important array, you never reveal the first record unless the guess is correct but for every guess you display the next record, the nuber of hints is equal to the array length - 1
    secretRow = []
        # record of the row numbers that have already been pulled, to reduce the long term memory usage.
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

    # look at the dictonary to see what password lists are present
    @staticmethod
    def getListOfPasswordTypes():
        dictonary = Path('dictonary')
        return dictonary.iterdir()

    # sets the new password file, and clears the class arrays
    def setPasswordFile(self, newPasswordFile):
        passwordFile = ""
        passwordFile = newPasswordFile
        pastRowNums = []
        secretRow = []
    # TESTING to validated outputs
    # getNextSecretRow()
    # getNextSecretRow()
    # getNextSecretRow()
# pwdHandeler = passwordAndHintHandeler()
# listOfPasswordFiles = pwdHandeler.getListOfPasswordTypes()
# for child in listOfPasswordFiles:
#     print("Child")
#     print(child)
#     pwdHandeler.setPasswordFile(child)
#     print("setPasswordFile")
#     print(pwdHandeler.passwordFile)
# main game loop for the project

#Authors:
    # Nicole Bromberek (Raven System)

# imports

    # for password handeling
import Group3_python as pwdHandeler
pwdHandeler = pwdHandeler.passwordAndHintHandeler()

    # for user interface views:
        #each view is a self contained loop.
def greater ():
    print("hello")

def difficultySelector ():
    print("hello")

def gameScreen():
    print("game")

def gameVictoryScreen():
    print("you win")

def gameDefeatScreen():
    print("you lose")

def askForReplay():
    print("play again?")

def replayGreeter():
    print("welcome back")

def exiter():
    print("goodby")


listOfPasswordFiles = pwdHandeler.getListOfPasswordTypes()
for child in listOfPasswordFiles:
    print("Child")
    print(child)
    pwdHandeler.setPasswordFile(child)
    print("setPasswordFile")
    print(pwdHandeler.passwordFile)
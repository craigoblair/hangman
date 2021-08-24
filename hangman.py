from os import system, name
from time import sleep
#These functions have been predefined
# define our clear function
from os import system
clear = lambda: system('clear')

def Welcome():
    print("*****************************************")
    print("*                                       *")
    print("*         Welcome to hangman            *")
    print("*                                       *")
    print("*****************************************")

def Goodbye():
    print("*****************************************")
    print("*                                       *")
    print("*      Thank you for using Hangman      *")
    print("*                                       *")
    print("*****************************************")

def GetWord():
    global enteredword
    enteredword=input("Please enter a word  ")
#    print("the word is", enteredword )
def GetWordLength():
    global lengthofword
    lengthofword=len(enteredword)
#    print("the word length is... ",lengthofword)
def DisplayUnderscores():
    print("__  " * lengthofword)
def GetLetters():
    global letter
    print();
    letter = input("Enter a letter ")
def CountLetters():
    for i in range(0,lengthofword):
        x = enteredword.count(letter)
        print("There are ",x ,"occurances of the letter ",letter )
        print("At the following positions ",[pos for pos, char in enumerate(enteredword) if char == letter])
        #print(enteredword.index(letter))
        GetLetters()
        print(x)

Welcome()
GetWord()
GetWordLength()
DisplayUnderscores()
GetLetters()
CountLetters()
#sleep(3)
#clear()
#Goodbye()

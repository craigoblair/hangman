#this is all about adding a letter to a variable
#next 2 lines are about importing a function from python
#that allows you to use the clear() command
from os import system
clear = lambda: system('clear')

#this function "getotherletters()"is for testing how to put letters
#into a variable that you might use, we use a for loop here to do the work
def getotherletters(): #define the function
    lengthofword=len(wrongletters)#get the length of wrongletters
    wrongmax=10        #this defines a varable to have a value of 10
                       #this determines how many incorrect letters you can enter
    for i in range(0,wrongmax):#do the loop upto wrongmax times, i.e. 10 times
        letter=input("Enter a letter  ") #get a letter from the user
        wrongletters=wrongletters[:len(wrongletters)] + letter #this is all
                            #about adding a letter to the end of wrongletters
        print(wrongletters.upper())#print the letters in uppercase

#This function getletters() is much the same concept as the one above except
#here we use a while loop here to do the work
def getletters(): #define the function
    wrongmax=10        #this defines a varable to have a value of 10
                       #this determines how many incorrect letters you can enter
    wrongletters="";   #set the variable wrongletters to have nothing in it
#    theword=input("enter a word  ")
#    lengthofword=len(theword)
    i=0                #set the variable "i" to 0
    while i < wrongmax:#while the variale "i" is less than the value of wrongmax
        clear()        #clears the screen
        print(wrongletters.upper()) #prints the letter in uppercase
        letter=input("Enter a letter  ")#get a letter from the user
        wrongletters=wrongletters[:len(wrongletters)] + letter #this is all
                            #about adding a letter to the end of wrongletters
        i=i+1 #increment the value of "i" by 1
        if i == wrongmanx: #test to see if "i" has the same value as wrongmax
            clear()        #clears the screen
            print("you lose, these are the letters you got wrong")
            print(wrongletters.upper()) #prints all the letters in uppercase
    #print(wrongletters)

#this function letterinword() is about finding a letter in a word
def letterinword():    #define the function
    i=0                #set the variable i to 0
    wrongmax=5         #set the variable wrongmax to 5
    theword = 'banana' #set the variable theword to "banana"
    letter = input('Enter a letter: ') # ask the user for a letter
    while i < wrongmax:#while the variale "i" is less than the value of wrongmax
        if letter in theword:#if the entered letter is in the variable "theword"
            print(letter)    #print the letter to the screen
        else:                #do this if it is not in the word
            i=i+1            #increment i by 1
            print(letter.upper()) #print the letter in uppercase
        letter = input('Enter a letter: ') # get a letter from the user
    input() #this just forces the user to hit enter to contnue

letterinword()      #this calls the function letterinword()
getotherletters()   #this calls the function getotherletters()
getletters()        #this calls the function getletters()

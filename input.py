# import only system from os, this allows us to clear within the program
from os import system
clear = lambda: system('clear')

#this bit works with text, you can type anything and it wont exit until you type "99"
clear() # clears the command prompt straight away
x = input("Enter text 99 to exit ") #asks for the user input before going into the while loop
while x != "99": #while the value of x is not equal to the string "99", python takes input as string by default
	clear() #clears the screen so the screen does not scroll
	x = input("Enter text 99 to exit ") #keeps asking the same question
clear() #clears the screen before going back to the caommand prompt

#this bit works with integers only, type text and it will chuck a wobbly
y = input("Enter the integer 99 to exit ")
y = (int(y)) #this converts the text input to integer, there is no error detection invovled here
while y != 99: #while the value of x is not equal to the string "99", python takes input as string by default
	clear() #clears the screen so the screen does not scroll
	y = input("Enter the integer 99 to exit ") #keeps asking the same question
	y = int(y)
clear() #clears the screen before going back to the command prompt

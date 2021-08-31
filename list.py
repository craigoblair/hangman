#This is a small tutorial on the why and wherefores of lists for hangman
#put content in the list
thislist = ["apple", "banana", "cherry"]
#-----------------------------------------
#print out the list with...
print(thislist)
#output is...
#['apple', 'banana', 'cherry']
#-----------------------------------------
#change the 0th element of the list, i.e the first one with an "a"
thislist[0]="a"
#print out the list with...
print(thislist)
#output is...
#['a', 'banana', 'cherry']
#-----------------------------------------
#put "__" into each element of the alist
#the number "6" can be replaced with the l;ength of the word
alist =["__"]*6
#print out the list with...
print(alist)
#output is...
#['__', '__', '__', '__', '__', '__']
#-----------------------------------------
#alternativly you can populate the list this away
#the "5" can be replaced with the length of the word-1
#e.g. "for i in range (0,lengthofword-1):"
#you can use this technique to populate the array to be seen on te screen reflecting the correct words
for i in range(0,5):
    alist[i]="a"
#print out the list with...
print(alist)
#output is...
#['a', 'a', 'a', 'a', 'a', '__']
#-----------------------------------------
#printing the list with out the "[]"looks like this
print(*alist,sep=',  ')
#output is...
#a,  a,  a,  a,  a,  __
#we still have commas sepearting the values
#so to  change this we remove the comma from sep and increase the spaces to suit
#you can also add and extra space at the begining to take output away from the edge of the screen
print("   ", *alist,sep='    ')
#output is...
#       a    a    a    a    a    __

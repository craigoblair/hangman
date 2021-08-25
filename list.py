thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[0]="a"
print(thislist)
alist =[]*6
print(alist)

i=0
for i in range(0,5):
    alist[i]='a'
print(alist)
print(*alist,sep =', ')

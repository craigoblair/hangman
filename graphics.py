def one():
    print("_____________ ")
def two():
    print("      |       ")
    print("      |       ")
    print("_____________ ")
def three():
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("_____________ ")
def four():
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("_____________ ")
def five():
    print("      _____   ")
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("_____________ ")
def six():
    print("      _____   ")
    print("      |    |  ")
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("_____________ ")
def seven():
    print("      _____   ")
    print("      |    |  ")
    print("      |    0  ")
    print("      |       ")
    print("      |       ")
    print("      |       ")
    print("_____________ ")
def eight():
    print("      _____   ")
    print("      |    |  ")
    print("      |    0  ")
    print("      |  --|--")
    print("      |       ")
    print("      |       ")
    print("_____________ ")


def nine():
    print("      _____   ")
    print("      |    |  ")
    print("      |    0  ")
    print("      |  --|--")
    print("      |    |  ")
    print("      |       ")
    print("_____________ ")
def ten():
    print("      _____   ")
    print("      |    |  ")
    print("      |    0  ")
    print("      |  --|--")
    print("      |    |  ")
    print("      |   / [ ")
    print("_____________ ")

x=0
count=0
while count < 10:
    clear()
    letter = input()
    if letter != "a":
        count = count + 1
        if count == 1:
            one()
        if count == 2:
            two()
        if count == 3:
            three()
        if count == 4:
            four()
        if count == 5:
            five()
        if count == 6:
            six()
        if count == 7:
            seven()
        if count == 8:
            eight()
        if count == 9:
            nine()
        if count == 10:
            ten()
    x = x + 1
    input()

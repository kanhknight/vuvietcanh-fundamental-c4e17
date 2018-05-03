from random import *
x = randint(0,100)
run = True
sai = 0
while run:
    sai +=1
    n = int(input("Guess my number (1 - 100)? "))
    if n==x:
        print("Bingo! Your Lucky number is: ",x)
        run = False
    if n>x:
        print("Too Large")
        print("You have {0} left!".format((8-sai)))
        if (8-sai)==0:
            print("You have {0} left!".format((8-sai)))
            run = False
    if n<x:
        print("Too Small")
        print("You have {0} left!".format((8-sai)))
        if (8-sai)==0:
            print("You have {0} left!".format((8-sai)))
            run = False

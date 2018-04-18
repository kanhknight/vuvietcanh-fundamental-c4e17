from random import *
guess = randint(0,100)
print("Now you think of a number from 0 to 100, then press \'Enter\'\nAll you need to do is to answer to my guess\n\'c\' if my guess is \'C\'orrect\n\'s\' if my guess is \'S\'maller than your number\n\'l\' if my guess is \'L\'arger than your number")

while True:
    ans = input("Is {0} your number? ".format(guess))
    if ans == "c":
        print("I Knew it!")
    if ans == "s":
        guess = randint(0,guess)
    if ans == "l":
        guess = randint(guess,100)     
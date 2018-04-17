from random import *
ran = randint(0,100)
print("Now think of a number from 0 to 100, then press 'Enter'")
while True:
    print("{0} là số mày đã có phải không?".format(ran))
    answer = input()
    if answer == "c":
        print("Đúng")
        print(ran)
        break
    if answer == "l":
        ran = (ran/2)
    if answer == "h":
        ran = (ran/2)
from random import *
a = randint(1,10)
b = randint(1,10)

while True:
    op = ["*","/","+","-"]
    result = 0
    op_rand = choice(op)

    if op_rand == "*":
        result = a * b
    elif op_rand == "/":
        result = a/b
    elif op_rand == "+":
        result = a+b
    elif op_rand == "-":
        result == a - b
    err = randint(-1,1)
    result_err = result + err
    print('{0} {1} {2} = {3}'.format(a,op_rand,b, result_err))
    print(result)

    answer = input('Y/N: ').upper()

    if result == result_err and answer == "Y":
        print("Đúng Rồi !")
    elif result != result_err and answer == "N":
        print("Đúng rồi !")
    else:
        print("Game Over !")
        break

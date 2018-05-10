from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1,10)
    y = randint(1,10)
    op = ["*","/","+","-"]
    result_right = 0
    op_rand = choice(op)

    if op_rand == "*":
        result_right = x * y
    elif op_rand == "/":
        result_right = x/y
    elif op_rand == "+":
        result_right = x+y
    elif op_rand == "-":
        result_right == x - y
    err = randint(-1,1)
    result = result_right + err
    return [x, y, op_rand, result]

def check_answer(x, y, op, result, user_choice):
    # User Choice : True/False
    real_result = 0
    if op == "*":
        real_result = x * y
    elif op == "/":
        real_result = x/y
    elif op == "+":
        real_result = x + y
    elif op == "-":
        real_result = x -y
    if real_result == result and user_choice == True:
        return True
    elif real_result !=result and user_choice == False:
        return True
    else:
        return False
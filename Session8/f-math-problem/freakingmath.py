from random import *

def calc(x,y,op):
    result = 0
    if op == "*":
        result = x * y
    elif op == "/":
        result = x/y
    elif op == "+":
        result = x + y
    elif op == "-":
        result = x -y
    return [x,y,op,result]

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1,10)
    y = randint(1,10)
    op_list = ["*","/","+","-"]
    op = choice(op_list)
    err = randint(-1,1)
    result = calc(x,y,op)
    result = result[3]
    result = result + err
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    # User Choice : True/False
    real_result = calc(x,y,op)
    if real_result[3] == result and user_choice == True:
        return True
    elif real_result[3] != result and user_choice == False:
        return True
    else:
        return False
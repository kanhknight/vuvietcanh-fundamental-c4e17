def cal(x,y,op):
    result  = 0
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    return result

print(__name__)
# Chỉ khi chạy trực tiếp thì mới chạy hàm dưới đây
if __name__ == "__main__":
     print("Eval imported!")
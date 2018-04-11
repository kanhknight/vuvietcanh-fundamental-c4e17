# Boolean values are True and False
# x == y -Produce True if ... x is equal to y
# x != y -... x is not equal to y
# x > y -... x is greater than y
# x < y -.. x is less than y
# x >= y -... x is greater than or equal to y
# x <= y -.. x is less than or equal to y
print("Ví dụ 1:")
n = float(input("Nhập vào số thứ nhất: "))
m = float(input("Nhập vào số thứ hai: "))
if n==m:
    print(bool(n==m))
    print("Hai số nhập vào bằng nhau")
elif n > m:
    print("Số thứ nhất lớn hơn")
    print(bool(n>m))
else:
    print("Số thứ nhất nhỏ hơn")
    print(bool(n<m))

test = []
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = 0.0
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = True
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))
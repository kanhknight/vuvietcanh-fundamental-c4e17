# Boolean values are True and False
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
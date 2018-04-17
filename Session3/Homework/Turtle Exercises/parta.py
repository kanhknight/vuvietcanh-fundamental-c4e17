from turtle import *
n = int(input("Nhập vào 1 số: "))
if n>=3:
    m = []
    for i in range(n):
        m.append(i+1)
    print(m)
    for j in m:
        if j == 3:
            for i in range(j):
                forward(100)
                left(360/j)
        if j>3:
            for i in range(j):
                forward(100)
                left(360/j)
    mainloop()
else:
    print("Nhập vào 1 số lớn hơn hoặc bằng 3")
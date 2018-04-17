from turtle import *
color_list = ['red','blue','brown','yellow','grey']
n = int(input("Nhập vào 1 số: "))
speed(0)
if n>=3:
    m = []
    pensize(2)
    for i in range(n):
        m.append(i+1)
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
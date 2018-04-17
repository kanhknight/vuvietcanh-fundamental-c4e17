from turtle import *
color_list = ['red','blue','brown','yellow','grey','green']
n = int(input("Enter Number: "))
speed(0)
for n in range(3,(n+1)):
    selected_color = color_list[(n-3)%len(color_list)]
    color(selected_color)
    pensize(2)
    for i in range(n):
        forward(10)
        left(360/n)
mainloop()
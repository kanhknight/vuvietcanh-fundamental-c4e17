from turtle import *
for i in range(0,500,3):
    speed(0)
    color("green")
    forward(i+30) 
    # có thể nhân i lên để tăng khoảng cách
    left(90)
mainloop()
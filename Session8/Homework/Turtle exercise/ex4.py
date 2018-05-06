from turtle import *

def draw_square(len_x,color_x):
    for i in range(4):
        speed(0)
        color(color_x)
        forward(len_x)
        left(90)

# TA's Code
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
    
mainloop()
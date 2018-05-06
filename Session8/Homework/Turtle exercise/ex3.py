from turtle import *

def square(len_x,color_x):
    for i in range(4):
        speed(0)
        color(color_x)
        forward(len_x)
        left(90)
    mainloop()
    
square(200,"blue")
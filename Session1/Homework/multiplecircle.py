from turtle import *
from math import *
t = Turtle()
t.speed(0)
t.color("green")
for i in range(8):
    for i in range(360):
        t.forward(1*tan(degrees(1)))
        t.right(1)
    t.right(+45)
mainloop()
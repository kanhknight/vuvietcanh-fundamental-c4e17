from turtle import *
speed(0)
color('blue')

def draw_star(x,y,length):
    goto(x,y)
    for i in range(5):
        pendown()
        forward(length)
        right(144)
        penup()

for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
mainloop()
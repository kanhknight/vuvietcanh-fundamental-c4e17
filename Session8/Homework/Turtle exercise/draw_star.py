import turtle 
star = turtle.Turtle()

# for i in range(50):
#     star.forward(50)
#     star.right(144)
    
# turtle.done()
def draw_star(x,y,length):
    star = turtle.Turtle()
    star.goto(x,y)
    for i in range(5):
        star.forward(length)
        star.right(144)
draw_star(-50,50,300)
turtle.mainloop()
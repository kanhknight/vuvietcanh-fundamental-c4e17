from turtle import *
colors = ['red','blue','brown','yellow','grey']
for i in range(len(colors)):
    fillcolor(colors[i])
    begin_fill()
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    right(90)
    end_fill()
    forward(50)
mainloop()
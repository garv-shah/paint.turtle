from turtle import Turtle, Screen

def dragging(x, y):
    yertle.ondrag(None)
    yertle.setheading(yertle.towards(x, y))
    yertle.goto(x, y)
    yertle.ondrag(dragging)

def clicking(x, y):
    yertle.penup()
    yertle.goto(x, y)
    yertle.pendown()

screen = Screen()

yertle = Turtle('turtle')
yertle.speed('fastest')

yertle.ondrag(dragging)
screen.onclick(clicking)

screen.mainloop()
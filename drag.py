from turtle import Turtle, Screen

MOVING, DRAGGING = range(2)


def move_handler(x, y):
    if state != MOVING:
        return

    onmove(screen, None)
    penTurtle.penup()
    penTurtle.setheading(penTurtle.towards(x, y))
    penTurtle.goto(x, y)
    onmove(screen, move_handler)


def click_handler(x, y):
    global state

    penTurtle.onclick(None)
    onmove(screen, None)

    penTurtle.onrelease(release_handler)
    penTurtle.ondrag(drag_handler)

    state = DRAGGING


def release_handler(x, y):
    global state

    penTurtle.onrelease(None)
    penTurtle.ondrag(None)

    penTurtle.onclick(click_handler)
    onmove(screen, move_handler)

    state = MOVING


def drag_handler(x, y):
    if state != DRAGGING:
        return

    penTurtle.ondrag(None)
    penTurtle.pendown()
    penTurtle.setheading(penTurtle.towards(x, y))
    penTurtle.goto(x, y)
    penTurtle.ondrag(drag_handler)


def onmove(self, fun, add=None):
    """
    >>> onmove(turtle.Screen(), lambda x, y: print(x, y))
    >>> screen.onmove(None)
    """

    if fun is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            fun(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)

        self.cv.bind('<Motion>', eventfun, add)


screen = Screen()
screen.setup(500, 600)
screen.screensize(1920, 1080)

penTurtle = Turtle()
penTurtle.speed('fastest')

state = MOVING

onmove(screen, move_handler)
penTurtle.onclick(click_handler)

screen.mainloop()

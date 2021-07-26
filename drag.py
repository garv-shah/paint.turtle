import turtle
import tkinter as tk

MOVING, DRAGGING = range(2)


def move_handler(x, y):
    if state != MOVING:
        return

    onmove(screen, None)
    permanent.penup()
    permanent.setheading(permanent.towards(x, y))
    permanent.goto(x, y)
    onmove(screen, move_handler)


def click_handler(x, y):
    global state

    permanent.onclick(None)
    onmove(screen, None)

    permanent.onrelease(release_handler)
    permanent.ondrag(drag_handler)

    state = DRAGGING


def release_handler(x, y):
    global state

    permanent.onrelease(None)
    permanent.ondrag(None)

    permanent.onclick(click_handler)
    onmove(screen, move_handler)

    state = MOVING


def drag_handler(x, y):
    if state != DRAGGING:
        return

    permanent.ondrag(None)
    permanent.pendown()
    permanent.setheading(permanent.towards(x, y))
    permanent.goto(x, y)
    permanent.ondrag(drag_handler)


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


root = tk.Tk()
root.title("paint.turtle")
canvas = tk.Canvas(root)
canvas.config(width=600, height=400)
canvas.pack(side=tk.LEFT)
screen = turtle.TurtleScreen(canvas)

permanent = turtle.RawTurtle(screen)
permanent.speed(0)

state = MOVING

onmove(screen, move_handler)
permanent.onclick(click_handler)

root.mainloop()

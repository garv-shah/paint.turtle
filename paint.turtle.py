import turtle
import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox

MOVING, DRAGGING = range(2)

pencolor = (0, 0, 0)
fillcolor = (0, 0, 0)
_fill = False


def oncontrolkeypress(self, fun, key):
    def eventfun(event):
        fun()

    self.getcanvas().bind("<Control-KeyPress-%s>" % key, eventfun)


def set_base_rect(x, y):
    temporary.penup()
    temporary.goto(x, y)
    temporary.pendown()
    global rect
    rect = [x, y]


def drag_rect(x, y):
    global pencolor
    global fillcolor
    temporary.ondrag(None)

    temporary.clear()
    temporary.color(pencolor)
    temporary.penup()
    temporary.goto(rect[0], rect[1])
    temporary.pendown()
    if _fill:
        temporary.fillcolor(fillcolor)
        temporary.begin_fill()
    temporary.goto(rect[0], y)
    temporary.goto(x, y)
    temporary.goto(x, rect[1])
    temporary.goto(rect[0], rect[1])
    if _fill:
        temporary.end_fill()

    temporary.ondrag(drag_rect)


def release_rect(x, y):
    temporary.clear()
    permanent.color(pencolor)
    permanent.penup()
    permanent.goto(rect[0], rect[1])
    permanent.pendown()
    if _fill:
        permanent.fillcolor(fillcolor)
        permanent.begin_fill()
    permanent.goto(rect[0], y)
    permanent.goto(x, y)
    permanent.goto(x, rect[1])
    permanent.goto(rect[0], rect[1])
    if _fill:
        permanent.end_fill()


def rectangle():
    off()
    temporary.ondrag(drag_rect)
    screen.onclick(set_base_rect)
    temporary.onrelease(release_rect)


def off():
    temporary.ondrag(None)
    screen.onclick(None)
    temporary.onrelease(None)
    onmove(screen, None)
    permanent.onclick(None)


def choose_color():
    global fillcolor
    global pencolor
    which_colour_change = messagebox.askyesnocancel("Question", "Select YES for Fill Colour\nSelect NO for Line Colour")

    if which_colour_change is not None:
        color_code = colorchooser.askcolor(title="Select color")[0]
        if which_colour_change:
            fillcolor = (int(color_code[0]), int(color_code[1]), int(color_code[2]))
        else:
            pencolor = (int(color_code[0]), int(color_code[1]), int(color_code[2]))

    print(which_colour_change)


def fill_on():
    global _fill
    _fill = True


def fill_off():
    global _fill
    _fill = False


def clear():
    permanent.clear()
    temporary.clear()


def undo():
    permanent.undo()


def pen_on():
    off()
    global state
    state = MOVING
    onmove(screen, move_handler)
    permanent.onclick(click_handler)


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
canvas.config(width=1100, height=700)
canvas.pack(side=tk.LEFT)
screen = turtle.TurtleScreen(canvas)
screen.colormode(255)
screen.bgcolor(225, 228, 232)

off_button = tk.Button(root, text="Off", command=off)
off_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

rectangle_button = tk.Button(root, text="Rectangle", command=rectangle)
rectangle_button.pack()

colour_button = tk.Button(root, text="Select color", command=choose_color)
colour_button.pack()

begin_fill_button = tk.Button(root, text="Fill On", command=fill_on)
begin_fill_button.pack()

end_fill_button = tk.Button(root, text="Fill Off", command=fill_off)
end_fill_button.pack()

pen_button = tk.Button(root, text="Pen", command=pen_on)
pen_button.pack()

screen.onkeypress(exit, 'x')
oncontrolkeypress(screen, undo, 'z')
screen.listen()
rect = [0, 0]

temporary = turtle.RawTurtle(screen)
permanent = turtle.RawTurtle(screen)
temporary.speed(0)
permanent.speed(0)
screen.delay(0)
root.mainloop()

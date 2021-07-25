import turtle

screen = turtle.Screen()


def onmove(self, fun, add=None):
    """
    Bind fun to mouse-motion event on screen.

    Arguments:
    self -- the singular screen instance
    fun  -- a function with two arguments, the coordinates
        of the mouse cursor on the canvas.

    Example:

    >>> onmove(turtle.Screen(), lambda x, y: print(x, y))
    >>> # Subsequently moving the cursor on the screen will
    >>> # print the cursor position to the console
    >>> screen.onmove(None)
    """

    if fun is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            fun(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)

        self.cv.bind('<Motion>', eventfun, add)


def goto_handler(x, y):
    onmove(turtle.Screen(), None)  # avoid overlapping events
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    onmove(turtle.Screen(), goto_handler)


def click_handler(x, y):
    print('click')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    onmove(screen, goto_handler)


def release_handler(x, y):
    print('release')
    onmove(screen, ())


turtle.shape('turtle')
turtle.speed(0)
turtle.delay(0)

screen.onclick(click_handler)
turtle.onrelease(release_handler)

turtle.mainloop()

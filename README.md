# paint.turtle
## project for coding and computers where i make an ms paint clone using turtle
<em> programming is boring so why not make a program to program for me </em>
<br>
This is for a school project of mine (definitely a WIP) where I use python turtle to recreate a more sophisticated drawing app such as MS Paint. The task for the project is essentially to make a promotional poster for a tourist attraction in Australia, which when done line by line in a beginner's programming class is excruciatingly boring. So, I present my solution: a program where you can just draw normally and it outputs Python Turtle code for you! My first idea was to just have a line detection algorithm or the sorts which just gets an image and draws it exactly in Turtle, but my teacher said that would bypass Turtle as a project requirment a bit too much. So then I introduced the idea above, and they said that as long as it's all done in Turtle, it's fine by them.

### How it works:
It's basically just a Turtle canvas within a Tkinter frame. Tkinter handles the button presses, and turtle handles the rest. Simple!

### What doesn't work yet:
Right now I'm struggling a lot with making a fluid pen tool like in MS Paint. The problem here is that the built in Turtle onClick() (or onPress, etc) aren't very accurate, in that they only work some of the time. I don't know if this is because I've implemented the code wrong, but it doesn't seem so so far. Dunno ¯\\\_(ツ)\_/¯


from graphics import *


def main():
    win = GraphWin('Shapes')
    # write code here
    center = Point(100,100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)
    ###Put a textual label in the center of the circle
    label = Text(center, "Red Circle")
    label.draw(win)
    ###Draw a square using a rectangle object
    rect = Rectangle(Point(30,30), Point(70,70))
    rect.draw(win)
    ##Draw a line segment using a Line object
    line = Line(Point(20,30), Point(180, 165))
    line.draw(win)
    ###Draw an oval using the obal object
    oval = Oval(Point(20,150), Point(180,199))
    oval.draw(win)

    # a graphics window will open when you run this program
    # to close the graphics window, you will need to click somewhere on the window
    # the two lines of code below are what will keep the graphics window open until after a mouse click
    win.getMouse()
    win.close()


main()

'''
from graphics import *


def main():
    win = GraphWin()
    # write code here
    leftEye = Circle(Point(80,50), 5)
    leftEye.setFill('yello')
    leftEye.setOutline('red')
    rightEye = leftEye.clone()
    rightEye.move(20.0)

    # a graphics window will open when you run this program
    # to close the graphics window, you will need to click somewhere on the window
    # the two lines of code below are what will keep the graphics window open until after a mouse click
    win.getMouse()
    win.close()


main()
'''
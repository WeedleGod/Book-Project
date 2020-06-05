from graphics import *


def main():
    win = GraphWin('Shapes')
    # write code here
    #Giant square for the backround
    rect = Rectangle(Point(0,0), Point(200,200))
    rect.setFill('aqua')
    rect.setOutline('aqua')
    rect.draw(win)
    #Circle for the sun
    center = Point(180,20)
    circ = Circle(center, 60)
    circ.setFill('yellow')
    circ.draw(win)
    #Rectangle for a field of grass
    rect = Rectangle(Point(200,160), Point(0,200))
    rect.setFill('green')
    rect.setOutline('green')
    rect.draw(win)
    

    # a graphics window will open when you run this program
    # to close the graphics window, you will need to click somewhere on the window
    # the two lines of code below are what will keep the graphics window open until after a mouse click
    win.getMouse()
    win.close()


main()
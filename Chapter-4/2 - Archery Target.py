from graphics import *

def main():
    win = GraphWin('Archery Target', 720, 720)
    win.setCoords(0,0,10,10)
    center = Point(5,5)

    white = Circle(Point(5,5), 4)
    white.setFill('white')
    white.draw(win)

    black = Circle(center, 3)
    black.setFill('black')
    black.draw(win)

    blue = Circle(center, 2)
    blue.setFill('blue')
    blue.draw(win)

    red = Circle(center, 1)
    red.setFill('red')
    red.draw(win)

    win.getMouse()
    win.close
main()
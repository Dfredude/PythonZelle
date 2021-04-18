from graphics import *
from math import *

def main():
    #Draw Window and set coordenates
    win = GraphWin('Draw a line', 720, 720)
    win.setCoords(0, 0, 10, 10)
    
    #Display text and input
    input_r_text = Text(Point(5, 8), """Click anywhere twice and see
    what you get""")
    input_r_text.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    p1x = p1.getX()
    p1y = p1.getY()
    p2x = p2.getX()
    p2y = p2.getY()
    #Draw Rectangle
    myrectangle = Rectangle(p1, p2)
    myrectangle.draw(win)
    #Get diferentials
    dx = p2x - p1x
    dy = p2y - p1y
    #Compute and print area
    area = dy * dx
    Text(Point(5, 3), 'The area is: ' + str(round(area, 2))).draw(win)
    #Compute and print perimeter
    perimeter = 2 * (dx + dy)
    Text(Point(5, 2), 'The length is: ' + str(round(perimeter, 2))).draw(win)
    # click mouse anywhere to close
    win.getMouse()
    win.close()


main()
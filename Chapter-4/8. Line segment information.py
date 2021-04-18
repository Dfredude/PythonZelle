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
    #Draw line
    myline = Line(p1, p2)
    myline.draw(win)
    print(p1, p2)
    #Get diferentials
    dx = p2x - p1x
    dy = p2y - p1y
    #Compute and print Slope
    slope = dy/dx
    Text(Point(5, 3), 'The Slope is: ' + str(round(slope, 2))).draw(win)
    #Compute and print length
    length = sqrt(dx**2 + dy**2)
    Text(Point(5, 2), 'The length is: ' + str(round(length, 2))).draw(win)
    #Get middle point
    mpx = (p1x + p2x)/2
    mpy = (p1y + p2y)/2
    #Draw middle point
    mp = Circle(Point(mpx, mpy), .1)
    mp.setFill('cyan')
    mp.draw(win)
    # click mouse anywhere to close
    win.getMouse()
    win.close()


main()
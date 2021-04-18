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
    p3 = win.getMouse()
    p1x, p1y = p1.getX(), p1.getY()
    p2x, p2y = p2.getX(), p2.getY()
    p3x, p3y = p2.getX(), p3.getY()
    #Draw Triangle
    myrectangle = Polygon(p1, p2, p3)
    myrectangle.draw(win)
    #Get diferentials
    p1p2_dx = p2x - p1x
    p1p2_dy = p2y - p1y
    p2p3_dx = p3x - p2x
    p2p3_dy = p3y - p2y
    p3p1_dx = p1x - p3x
    p3p1_dy = p1y - p3y 
    #Compute and print perimeter
    lp1p2 = sqrt(p1p2_dx**2 + p1p2_dy**2)
    lp2p3 = sqrt(p2p3_dx**2 + p2p3_dy**2)
    lp3p1 = sqrt(p3p1_dx**2 + p3p1_dy**2)
    perimeter = lp1p2 + lp2p3 + lp3p1
    Text(Point(5, 2), 'The length is: ' + str(round(perimeter, 2))).draw(win)
    #Compute area
    s = (lp1p2 + lp2p3 + lp3p1)/2
    area = sqrt(s*(s-lp1p2)*(s-lp2p3)*(s-lp3p1))
    Text(Point(5, 3), 'The area is: ' + str(round(area, 2))).draw(win)
    # click mouse anywhere to close
    win.getMouse()
    win.close()


main()
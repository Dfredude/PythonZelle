from math import *
from graphics import *
def triangleAreaSidesLengths(a ,b, c):
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c)) 

def get_and_draw_point(win):
    point = win.getMouse()
    point.draw(win)
    return point

def distance(p1, p2):
    return sqrt((p2.getX()-p1.getX())**2 + (p2.getY()-p1.getY())**2)

def main():
    #Draw window
    win = GraphWin('Draw triangle', 1280, 720)
    win.setCoords(0,0,10,10)
    #Draw intro message
    intro_msg = Text(Point(5, 0.5), 'Click on 3 points')
    intro_msg.draw(win)
    #Get point input from user and draw it
    p1 = get_and_draw_point(win)
    p2 = get_and_draw_point(win)
    p3 = get_and_draw_point(win)
    #Draw triangle using 3 inputs
    triangle = Polygon(p1, p2, p3)
    triangle.setFill('peachpuff')
    triangle.setOutline('cyan')
    triangle.draw(win)
    #Calculations
    a, b, c = distance(p1, p2), distance(p2, p3), distance(p3, p1)
    perimeter = a + b + c
    print(a,b,c)
    area = triangleAreaSidesLengths(a, b, c)
    intro_msg.setText('The perimeter is: {0:0.2f} and area is: {1:0.2f}'.format(perimeter, area))
    win.getMouse()
    win.close()

main()
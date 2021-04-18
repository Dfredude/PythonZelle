from graphics import *

def main():
    win = GraphWin('Winter',720,720)
    win.setCoords(0,0,10,10)

    tsquare = Rectangle(Point(1.5, 1.5), Point(3, 3))
    tsquare.setFill('brown')
    tsquare.draw(win)

    ttriangle1 = Polygon(Point(.5, 3),Point(4, 3),Point(2.25, 6.5))
    ttriangle1.setFill('green')
    ttriangle1.draw(win)

    ttriangle2 = Polygon(Point(1, 4.5),Point(3.5, 4.5),Point(2.25, 7))
    ttriangle2.setFill('green')
    ttriangle2.draw(win)

    ttriangle3 = Polygon(Point(1.5, 6),Point(3, 6),Point(2.25, 8))
    ttriangle3.setFill('green')
    ttriangle3.draw(win) 

    sman_circle1 = Circle(Point(7,3), 2)
    sman_circle1.setFill('white')
    sman_circle1.draw(win)

    sman_circle2 = Circle(Point(7,5), 1.5)
    sman_circle2.setFill('white')
    sman_circle2.draw(win)

    sman_circle3 = Circle(Point(7, 6.5), 1.2)
    sman_circle3.setFill('white')
    sman_circle3.draw(win)

    sman_eye1 = Circle(Point(6.5, 7), .25)
    sman_eye1.setFill('black')
    sman_eye1.draw(win)

    sman_eye2 = Circle(Point(7.5, 7), .25)
    sman_eye2.setFill('black')
    sman_eye2.draw(win)
    
    sman_mouthc = Circle(Point(7,6.2), .5)
    sman_mouthc.setFill('white')
    sman_mouthc.draw(win)

    sman_mouthr = Rectangle(Point(6.5, 6.2), Point(7.5, 6.7))
    sman_mouthr.setFill('white')
    sman_mouthr.setOutline('white')
    sman_mouthr.draw(win)
    win.getMouse()

main()
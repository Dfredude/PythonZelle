from graphics import *
import math as m

def C_CurveAlgorithm(turtle, length, degree):
    if degree == 0:
        turtle.draw(length)
    else:
        Nlength = length/m.sqrt(length)
        Ndegree = degree-1
        turtle.turn(45)
        C_CurveAlgorithm(turtle, Nlength, Ndegree)
        turtle.turn(-90)
        C_CurveAlgorithm(turtle, Nlength, Ndegree)
        turtle.turn(45)
        
class Turtle():
    def __init__(self, win, point) -> None:
        self.win = win
        self.location = point
        self.direction = 1.56

    def moveTo(self, somePoint):
        self.location = somePoint

    def draw(self, length):
        dx, dy = self.getDxDy(length)
        newLocation = Point(self.location.getX()+dx, self.location.getY()+dy)
        Line(self.location, newLocation).draw(self.win)
        self.moveTo(newLocation)

    def turn(self, degrees):
        self.direction += m.radians(degrees)

    def getDxDy(self, length):
        dx = length * m.cos(self.direction)
        dy = length * m.sin(self.direction)
        return dx, dy


def main():
    length = 720
    degree = 14
    win = GraphWin("Koch Algorithm",720, 480)

    turtle = Turtle(win, Point(350, 150))
    C_CurveAlgorithm(turtle, length, degree)
    win.getMouse()

main()
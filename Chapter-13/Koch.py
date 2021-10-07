from graphics import *
import math as m

def kochAlgorithm(turtle, length, degree):
    if degree == 0:
        turtle.draw(length)
    else:
        Nlength = length/3
        Ndegree = degree-1
        kochAlgorithm(turtle, Nlength, Ndegree)

class Turtle():
    def __init__(self, win, point) -> None:
        self.win = win
        self.location = point
        self.direction = 0

    def moveTo(self, somePoint):
        self.location = somePoint

    def draw(self, length):
        dx, dy = self.getDxDy(length)
        newLocation = Point(self.location.getX()+dx, self.location.getY()+dy)
        Line(self.location, newLocation).draw(self.win)
        self.moveTo(newLocation)
        if self.direction == 0: self.direction = -60
        elif self.direction == -60: self.direction = 60
        else: self.direction = 0

    def turn(self, degrees):
        self.direction += m.radians(degrees)

    def getDxDy(self, length):
        dx = length * m.cos(self.direction)
        dy = length * m.sin(self.direction)
        return dx, dy


def main():
    length = 500
    degree = 0
    win = GraphWin("Koch Algorithm",720, 480)
    win.setCoords(0,0,1000,1000)
    kochAlgorithm(Turtle(win, Point(250,800)), length, degree)
    win.getMouse()

main()
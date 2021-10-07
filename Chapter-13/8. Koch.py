from graphics import *
import math as m

def kochAlgorithm(turtle, length, degree):
    if degree == 0:
        turtle.draw(length)
    else:
        Nlength = length/3
        Ndegree = degree-1
        kochAlgorithm(turtle, Nlength, Ndegree)
        turtle.turn(60)
        kochAlgorithm(turtle, Nlength, Ndegree)
        turtle.turn(-120)
        kochAlgorithm(turtle, Nlength, Ndegree)
        turtle.turn(60)
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

    def turn(self, degrees):
        self.direction += m.radians(degrees)

    def getDxDy(self, length):
        dx = length * m.cos(self.direction)
        dy = length * m.sin(self.direction)
        return dx, dy


def main():
    length = 600
    degree = 4
    win = GraphWin("Koch Algorithm",1080, 720)
    turtle = Turtle(win, Point(200,550))
    for i in range(3):
        kochAlgorithm(turtle, length, degree)
        turtle.turn(-120)
    win.getMouse()

main()
from graphics import *

class temp:
    def __init__(self) -> None:    
        self.win = GraphWin('Projectile Animation', 720, 480)
        self.win.setCoords(0, 0, 100, 100)
        Line(Point(10, 10), Point(100, 10)).draw(self.win)
        for x in range(0, 210, 50):
            Text(Point(x, -7), str(x)).draw(self.win)
            Line(Point(x, 0), Point(x, 2)).draw(self.win)
        self.win.getMouse()

if __name__ == '__main__': temp()


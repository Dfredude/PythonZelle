from graphics import *
import random as r
def drawWindow():
    win = GraphWin('Get pi using Monte Carlo simulation', 720, 480)
    win.setCoords(-1,-1,1,1)
    return win

def getInput(point, win):
    pX = point.getX()
    pY = point.getY()
    input_box = Entry(point, 5)
    input_text = Text(Point(pX, pY+.5), 'Enter number of darts to be thrown')
    input_box.draw(win)
    input_text.draw(win)
    key = win.getKey()
    while key != 'Return':
        key = win.getKey()
    return int(input_box.getText())
    input_box.undraw()

def drawCircle(win):
    center = Point(0, 0)
    red = Circle(center, 1)
    red.setFill('red')
    red.draw(win)

def simulateNDartsThrown(n, win):
    h = 0
    for i in range(n):
        dart = Point(2*r.random()-1, 2*r.random()-1)
        dart.draw(win)
        if dart.getX()**2 + dart.getY()**2 <= 1:
            h += 1
    return h

def drawOutput(win, darts_thrown_in_circle, n):
    output_text = Text(Point(0, -.5), 'Estimated pi is: {0:0.3f}'.format(4*darts_thrown_in_circle/n))
    output_text.setTextColor('blue')
    output_text.draw(win)


def main():
    win = drawWindow()
    n = getInput(Point(0,0),win )
    drawCircle(win)
    darts_thrown_in_circle = simulateNDartsThrown(n, win)
    drawOutput(win, darts_thrown_in_circle, n)
    win.getMouse()
    win.close

main()
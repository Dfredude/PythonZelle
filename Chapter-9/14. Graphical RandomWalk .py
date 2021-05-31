from graphics import *
import random as r
import math as m
def drawWindow():
    win = GraphWin('Random Walk', 480, 480)
    win.setCoords(-50,-50,50,50)
    return win

def getInput(win):
    input_box = Entry(Point(0,0), 5)
    input_box.setText('0')
    input_text = Text(Point(0, 20), 'Enter the amount of steps you want to take')
    input_text.setTextColor('blue')
    input_box.draw(win)
    input_text.draw(win)
    key = win.getKey()
    while key != 'Return':
        key = win.getKey()
    input_box.undraw()
    input_text.undraw()
    return int(input_box.getText())

def simRandomWalk(win, n):
    initial_position = Point(0,0)
    initial_position.draw(win)
    for i in range(n):
        step_point = step(initial_position)
        Line(initial_position, step_point).draw(win)
        initial_position = step_point
        update(30)
        
def step(point):
    x = point.getX()
    y = point.getY()
    angle = r.random()*2*m.pi
    return Point(x+m.cos(angle), y+m.sin(angle))

def main():
    win = drawWindow()
    n = getInput(win)
    simRandomWalk(win, n)
    win.getMouse()


main()
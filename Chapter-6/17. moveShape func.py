from graphics import *

def moveTo(shape, newCenter):
    shape_center = shape.getCenter()
    shape_centerX = shape_center.getX()
    shape_centerY = shape_center.getY()
    new_centerX = newCenter.getX()
    new_centerY = newCenter.getY()
    dx = new_centerX - shape_centerX
    dy = new_centerY - shape_centerY
    shape.move(dx, dy)

def main():
    win = GraphWin('Move shapes', 1280, 720)
    center = win.getMouse()
    circle = Circle(center, 100)
    circle.draw(win)
    for i in range(10):
        center = win.getMouse()
        moveTo(circle, center)
    win.getMouse()

main()
        

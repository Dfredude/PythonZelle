from tkinter.constants import W, Y
from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        '''Creates a rectangular button'''
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        '''Returns the label string of this button.'''
        return (self.active and self.xmin <= p.getX() <= self.xmax and
        self.ymin <= p.getY() <= self.ymax)
    
    def getLabel(self):
        "Returns the label string of this button"
        return self.label.getText()

    def getStatus(self):
        'Returns wether button is active'
        return self.active

    def activate(self):
        'Sets this button to "active".'
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        'Sets this button to "inactive".'
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

class Door:
    def __init__(self, point, win, width, height, door_num) -> None:
        #Set variables values
        self.num = door_num
        self.active = 0
        self.width, self.height = width, height
        self.X, self.Y = point.getX(), point.getY()
        #Draw Rectangle
        self.rec = Rectangle(Point(self.X - self.width/2, self.Y - self.height/2),
        Point(self.X + self.width/2, self.Y + self.height/2)).draw(win) 
        #Draw door knob
        self.knob = Circle(Point(self.rec.getCenter().getX() + self.width/4, self.rec.getCenter().getY()), width/10)
        self.knob.draw(win)

    def activate(self): self.active = True

    def getActive(self): return self.active

    def getCenter(self):return self.rec.getCenter()

    def getX(self): return self.X
    
    def getY(self): return self.Y

    def getWidth(self): return self.width

    def getHeight(self): return self.height

    def getDoorNum(self): return int(self.num)

    def openDoor(self):
        self.rec.setFill('gray')
        self.rec.setOutline('black')
        self.rec.setWidth(2)
        self.knob.undraw()
    
    def undraw(self):
        self.rec.undraw()
        self.knob.undraw()
from graphics import *
from widgets import Button
from random import randrange

class Face:
    def __init__(self, window, center, size) -> None:
        self.smile_status, self.frown_status = False, False
        self.win = window
        self.center = center
        self.size = size
        self.eyeSize = eyeSize = .15*size
        eyeOff = size/3
        mouthSize = .8*size
        mouthOff = size/2
        self.head = Circle(center, size)
        self.head.setFill('white')
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        self.p1 = center.clone()
        self.p1.move(-mouthSize/2, -mouthOff)
        self.p2 = center.clone()
        self.p2.move(mouthSize/2, -mouthOff)
        self.mouth = Line(self.p1, self.p2)
        self.mouth.draw(window)
        self.line_length = self.p2.getX()-self.p1.getX()
    
    def smile(self):
        self.mouth.undraw()
        self.smiley_radius = self.line_length/2
        self.smiley = Circle(Point(self.p1.getX()+self.line_length/2, self.p1.getY()), self.smiley_radius)
        self.smiley.draw(self.win)
        self.smileyX = self.smiley.getCenter().getX()
        self.smileyY = self.smiley.getCenter().getY()
        self.ontop = Rectangle(Point(self.smileyX-self.smiley_radius, self.smileyY), 
        Point(self.smileyX+self.smiley_radius, self.smileyY+self.smiley_radius))
        self.ontop.setFill('white')
        self.ontop.setOutline('white')
        self.ontop.draw(self.win)
        self.smile_status = True
    
    def frown(self):
        lp1 = self.leftEye.getCenter().clone()
        lp2 = self.leftEye.getCenter().clone()
        rp1 = self.rightEye.getCenter().clone()
        rp2 = self.rightEye.getCenter().clone()
        lp1.move(-self.size*.12, self.eyeSize*2)
        lp2.move(self.size*.25, self.eyeSize*.2)
        rp1.move(-self.size*.25, self.eyeSize*.2)
        rp2.move(self.size*.12, self.eyeSize*2)
        self.leyebrow = Line(lp1, lp2)
        self.leyebrow.draw(self.win)
        self.reyebrow = Line(rp1, rp2)
        self.reyebrow.draw(self.win)
        self.frown_status = True

    def reset(self):
        if self.frown_status == True:
            self.leyebrow.undraw()
            self.reyebrow.undraw()
            self.frown_status = False
        if self.smile_status == True:
            self.smiley.undraw()
            self.ontop.undraw()
            self.mouth.draw(self.win)
            self.smile_status = False
        else: pass
    
    def getX(self): return self.head.getCenter().getX()

    def getY(self): return self.head.getCenter().getY()

    def move(self, dx, dy):
        self.head.move(dx, dy)
        self.leftEye.move(dx, dy)
        self.rightEye.move(dx, dy)
        if self.smile_status == True:
            self.ontop.move(dx, dy)
            self.smiley.move(dx, dy)
        else:
            self.mouth.move(dx, dy)
            if self.frown_status == True: 
                self.leyebrow.move(dx, dy)
                self.reyebrow.move(dx, dy)


def main():
    win = GraphWin('Face', 720, 720)
    win.setCoords(0,0,100,100)
    myFace = Face(win, Point(65, 50), 25)
    quitb = Button(win, Point(80, 15), 10, 10, 'Quit')
    quitb.activate()
    quit = False
    dx, dy = .01, .01
    faces = ['frown', 'reset', 'smile']
    while quit == False:
        facechange = True 
        x = myFace.getX() 
        y = myFace.getY()
        if x <= 25: dx = 1
        if x >= 75: dx = -1
        if y <= 25: dx = 1
        if y >= 75: dx = -1
        else: facechange = False
        if facechange == True:
            numrand = randrange(0,3)
            if numrand == 0: myFace.reset()
            elif numrand == 1: 
                myFace.reset()
                myFace.smile()
            else: 
                myFace.reset()
                myFace.frown()
        myFace.move(dx, dy)
        update(600)

        

main()
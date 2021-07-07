from tkinter.constants import FALSE, NORMAL, TRUE
from graphics import *
from widgets import Button

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

    def getY(self): return self.head.getCenter().getX()

    

def main():
    win = GraphWin('Face', 720, 720)
    win.setCoords(0,0,100,100)
    myFace = Face(win, Point(50, 50), 25)
    smileb = Button(win, Point(20,15), 10, 10, 'Smile')
    smileb.activate()
    frownb = Button(win, Point(30, 15), 10, 10, 'Frown')
    frownb.activate()
    normalb = Button(win, Point(40, 15), 10, 10, 'Normal')
    normalb.activate()
    quitb = Button(win, Point(80, 15), 10, 10, 'Quit')
    quitb.activate()
    quit = False
    while quit == False:
        click = win.getMouse()
        if smileb.clicked(click):
            myFace.reset()
            myFace.smile()
        elif frownb.clicked(click): 
            myFace.reset()
            myFace.frown()
        elif normalb.clicked(click):
            myFace.reset()
        elif quitb.clicked(click):
            win.close()
            quit = True
        
    
main()
    
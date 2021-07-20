from graphics import *

class GraphicsGroup:
    def __init__(self, anchor:Point) -> None:
        self.anchor = anchor
        self.objects = []
    
    def getAnchor(self): return self.anchor

    def addObject(self, gObject): self.objects.append(gObject)

    def move(self, dx, dy): 
        for obj in self.objects: obj.move(dx, dy) 
        self.anchor.move(dx, dy)
    
    def draw(self, win):
        for obj in self.objects: obj.draw(win)

    def undraw(self):
        for obj in self.objects: obj.undraw()

def main():
    win = GraphWin('lol')
    win.setCoords(0,0,100,100)
    myObjects = GraphicsGroup(Point(50,50))
    myObjects.addObject(Circle(myObjects.getAnchor(), 10))
    myObjects.addObject(Line(Point(30,40), Point(60,70)))
    myObjects.draw(win)
    win.getMouse()
    myObjects.move(5, 40)
    win.getMouse()

if __name__ == '__main__': main()
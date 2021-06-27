from graphics import *
class DieView:
    'Widget that displays a graphical representation of a dice'
    def __init__(self, win, center, size) -> None:
        'Create a view of a die, e.g.: d1 = DieView(mywin, Point(40,50), 20)'
        self.win = win
        self.background = 'white' #color of die face
        self.foreground = 'black' #color of the pips
        self.psize = 0.1 * size
        hsize = size/2
        offset = 0.6 * hsize

        #create square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        #Create 7 circles for standard pip locations
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)

    def __makePip(self, x, y):
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

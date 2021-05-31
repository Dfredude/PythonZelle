from graphics import *
from math import *
from widgets import Button
def drawFace(center, size, win):
    head = Circle(center, size)
    head.draw(win)
    difference = size/3.5
    eyes_radius = size/6
    centerX = center.getX()
    centerY = center.getY()
    eye1 = Circle(Point(centerX+difference, centerY+difference), eyes_radius)
    eye2 = Circle(Point(centerX-difference, centerY+difference), eyes_radius)
    smile = Line(Point(centerX-difference, centerY-difference), Point(centerX+difference, centerY-difference))
    eye1.draw(win)
    eye2.draw(win)
    smile.draw(win)

def distance(p1, p2):
    return sqrt((p2.getX()-p1.getX())**2 + (p2.getY()-p1.getY())**2)

def main():
    #Define variables
    default_width = 720
    default_height = 480
    #Draw window
    win = GraphWin('Draw smiley faces on your picture', default_width, default_height)
    win.setCoords(0,0,100,100)
    #First scene creation
    general_text = Text(Point(50, 50), 'How many faces do you want a draw?')
    input_box = Entry(Point(50, 40), 2)
    input_box.setText('0')
    #First scene draw
    general_text.draw(win)
    input_box.draw(win)
    continue_button = Button(win, Point(50, 25), 10, 10, 'Continue')
    continue_button.activate()
    while continue_button.clicked(win.getMouse()) == False: pass
    #Second scene draw
    win.close()
    img = Image(Point(50, 50), 'img.gif')
    img_width = img.getWidth()
    img_height = img.getHeight()
    smileys_window = GraphWin('Draw it now!', img_width, img_height)
    smileys_window.setCoords(0,0,100,100)
    img.draw(smileys_window)
    number_of_circles = input_box.getText()
    general_text.draw(smileys_window)
    general_text.setText('One click for center, another for radius, you can do it {0} times to draw {0} circles'.format(number_of_circles))
    input_box.undraw()
    for i in range(int(number_of_circles)):
        center = smileys_window.getMouse()
        radius_coor = smileys_window.getMouse()
        radius = distance(center, radius_coor)
        drawFace(center, radius, smileys_window)
    smileys_window.getMouse() or smileys_window.getKey()

main()

        
        


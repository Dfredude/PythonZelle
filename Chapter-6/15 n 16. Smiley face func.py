from graphics import *
from math import *
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

def button(text, button_text_X_point, button_text_Y_point, graphicwindow, X_dif, Y_dif):
    #Create button text
    button_text = Text(Point(button_text_X_point, button_text_Y_point), text)
    button_text.draw(graphicwindow)
    #Draw box
    y_top = button_text_Y_point + Y_dif
    y_bottom = button_text_Y_point - Y_dif
    box = Rectangle(Point(button_text_X_point-X_dif,y_bottom),Point(button_text_X_point+X_dif,y_top))
    box.setOutline('blue')
    box.draw(graphicwindow)
    click = graphicwindow.getMouse()
    xcor = click.getX()
    ycor = click.getY()
    if xcor <= button_text_X_point+X_dif and xcor >= button_text_X_point-X_dif and ycor <= y_top and ycor >= y_bottom:
        box.undraw()
        button_text.undraw()
        boolean = 1
        return boolean

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
    boolean = 0
    boolean = button('Continue', 50, 30, win, 5, 5)
    if boolean == True:
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
    smileys_window.getMouse()

main()

        
        


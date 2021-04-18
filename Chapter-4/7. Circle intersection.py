from graphics import *
from math import *

def main():
    #Draw Window and set coordenates
    win = GraphWin('Circle intersection', 720, 720)
    win.setCoords(-10, -12, 10, 10)
    
    #Display text and input
    input_r_text = Text(Point(0,8), "Enter radius: ")
    radius = Entry(Point(0, 7), 5)
    radius.setText('0.0')
    input_r_text.draw(win)
    radius.draw(win)
    input_y_text = Text(Point(0,6), "Enter y intersection(From -10 to 10): ")
    yintercept = Entry(Point(0, 5), 5)
    yintercept.setText('0.0')
    input_y_text.draw(win)
    yintercept.draw(win)
    quit_text = Text(Point(0, -5), 'Click two times anywhere to quit')
    quit_text.draw(win)
    
    #Draw button to continue
    changescene = GetResultButton(0, 3.5, win, 2, .5)
    
    #If button is pressed the function returns a value of 1 which we use for a boolean statement
    if changescene == 1:
        print(changescene)
        #Convert variab to floats
        radiusft = float(radius.getText())
        yinterceptft = float(yintercept.getText())
        #Compute x
        first_x = sqrt(radiusft**2 - yinterceptft**2 )
        second_x = -sqrt(radiusft**2 - yinterceptft**2 )
        #Undraw first scene
        input_r_text.undraw()
        radius.undraw()
        input_y_text.undraw()
        yintercept.undraw()
        quit_text.undraw()
        #Draw axis
        axis_x = Line(Point(-10,0),Point(10,0))
        axis_x.setArrow('last') 
        axis_y = Line(Point(0,-10), Point(0, 10))
        axis_y.setArrow('last')
        axis_x.draw(win)
        axis_y.draw(win)
        #Draw circle
        Circle(Point(0,0), radiusft).draw(win)
        #Draw line
        line_interception = Line(Point(-10, yinterceptft), Point(10, yinterceptft))
        line_interception.setOutline('Blue')
        line_interception.draw(win)
        #Draw intersecting points
        int1 = Circle(Point(first_x, yinterceptft), .2)
        int1.setFill('red')
        int1.draw(win)
        int2 = Circle(Point(second_x, yinterceptft), .2)
        int2.setFill('red')
        int2.draw(win)
        #Output x results
        Text(Point(-5, -11), 'The x values are: ' + str(round(first_x, 2)) + ' and ' + str(round(second_x, 2))).draw(win)

    # click mouse anywhere to close
    win.getMouse()
    win.close()

def GetResultButton(button_text_X_point, button_text_Y_point, graphicwindow, X_dif, Y_dif):
    #Create button text
    button_text = Text(Point(button_text_X_point, button_text_Y_point),'Get result')
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
        changescene = 1
        return changescene

main()
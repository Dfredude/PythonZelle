from graphics import *
import math as m

def squareEach(numbers):
    return [i**2 for i in numbers]

def button(text, button_text_X_point, button_text_Y_point, graphicwindow, X_dif, Y_dif):
    #Create button text
    button_text = Text(Point(button_text_X_point, button_text_Y_point), text)
    #Draw box
    y_top = button_text_Y_point + Y_dif
    y_bottom = button_text_Y_point - Y_dif
    box = Rectangle(Point(button_text_X_point-X_dif,y_bottom),Point(button_text_X_point+X_dif,y_top))
    box.setOutline('blue')
    box.setFill('white')
    box.draw(graphicwindow)
    button_text.draw(graphicwindow)
    click = graphicwindow.getMouse()
    xcor = click.getX()
    ycor = click.getY()
    if xcor <= button_text_X_point+X_dif and xcor >= button_text_X_point-X_dif and ycor <= y_top and ycor >= y_bottom:
        box.undraw()
        button_text.undraw()
        return True
    else: return click

def main():
    win = GraphWin('Regression line plot', 720, 480)
    win.setCoords(0, 0, 10, 10)
    points_list, x_list, y_list, xy_list = [], [], [], []
    done = False
    while done != True:
        done = button('Done', 1, 1, win, .5, .5)
        if done == True: break
        point = done
        point.draw(win)
        points_list.append(point)
        print(done)
    for i in points_list:
        x = i.getX()
        y = i.getY()
        xy = x * y
        x_list.append(x)
        y_list.append(y)
        xy_list.append(xy)
    n = len(points_list)
    x_average = sum(x_list)/n
    y_average = sum(y_list)/n
    x_sq_list = squareEach(x_list)
    x_sq_mean = sum(x_sq_list)/n
    xy_mean = sum(xy_list)/n
    m = (x_average * y_average - xy_mean) / (x_average**2 - x_sq_mean)
    print(m)
    y_start = y_average - m * x_average
    y_finish = y_start + m*10
    first_point = Point(0, y_start)
    second_point = Point(10, y_finish)
    Line(first_point, second_point).draw(win)
    win.getMouse()

main()
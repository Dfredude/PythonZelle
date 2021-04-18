from graphics import *
from math import *

def main():
    #Draw Window and set coordenates
    win = GraphWin('Draw a line', 720, 720)
    win.setCoords(0, 0, 10, 10)
    
    #Display text
    input_r_text = Text(Point(5, 8), "Click anywhere 5 times")
    input_r_text.draw(win)
    #Get first two inputs and their x and y values
    r1 = win.getMouse()
    r2 = win.getMouse()
    r1X = r1.getX()
    r1Y = r1.getY()
    r2X = r2.getX()
    r2Y = r2.getY()
    #Draw house frame
    frame = Rectangle(r1, r2)
    frame.draw(win)
    #Get door top center point and its x and y coordenates
    dtc = win.getMouse()
    dtcX = dtc.getX()
    dtcY = dtc.getY()
    #Draw door
    houese_frame_width = r2X - r1X
    doorwidth = houese_frame_width/5
    door = Rectangle(Point(dtcX+(doorwidth/2), dtcY), Point(dtcX-(doorwidth/2), r1Y))
    door.draw(win)
    #Get center of squared window and x and y values
    window_center = win.getMouse()
    window_center_X = window_center.getX()
    window_center_Y = window_center.getY()
    #Draw squared window
    window_width = doorwidth/2
    window = Rectangle(Point(window_center_X + window_width, window_center_Y + window_width), 
    Point(window_center_X - window_width, window_center_Y - window_width))
    window.draw(win)
    #Get roof peak
    roofpeak = win.getMouse()
    #Draw roof
    roof = Polygon(roofpeak, r2, Point(r1X, r2Y))
    roof.draw(win)
    win.getMouse()
    win.close
main()
from graphics import GraphWin, Point
from widgets import CButton
'Testing CButton object'
def main():
    win = GraphWin('CButton', 480, 480)
    win.setCoords(0,0,100,100)
    my_button = CButton(win, Point(50,50), 20, 'Close')
    my_button.activate()
    while my_button.clicked(win.getMouse()) == False:
        pass
    win.close

main()

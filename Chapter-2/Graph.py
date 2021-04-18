from graphics import  *

def textInp():
    win = GraphWin('Click and type', 500, 500)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)

textInp()
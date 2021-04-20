from graphics import *

def handleClick(pt, win):
    info = Entry(pt, 10)
    info.draw(win)
    status = True
    while True:
        key = win.getKey()
        if key == 'Escape':
            status = False
            break
        elif key == 'Return':
            break
    
    if status == True:
        info.undraw()
        typed = info.getText()
        return typed
    
def main():
    win = GraphWin('Test', 720, 480)
    print(handleClick(Point(360, 240), win))

main()
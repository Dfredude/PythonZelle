from graphics import *

def main():
    win = GraphWin('Archery Target', 720, 720)
    win.setCoords(0,0,10,10)
    center = Point(5,5)

    white = Circle(Point(5,5), 4)
    white.setFill('white')
    white.draw(win)

    black = Circle(center, 3)
    black.setFill('black')
    black.draw(win)

    blue = Circle(center, 2)
    blue.setFill('blue')
    blue.draw(win)

    red = Circle(center, 1)
    red.setFill('red')
    red.draw(win)

    score = 0

    score_text = Text(Point(5, 9.5), 'Your current score: {0}'.format(score))
    score_text.draw(win)
    for i in range(5):
        arrow = win.getMouse()
        arrowX = arrow.getX()
        arrowY = arrow.getY()
        if arrowX <= 6 and arrowX >= 4 and arrowY <= 6 and arrowY >= 4:
            score += 9
        elif arrowX <= 7 and arrowX >= 3 and arrowY <= 7 and arrowY >= 3:
            score += 7
        elif arrowX <= 8 and arrowX >= 2 and arrowY <= 8 and arrowY >= 2:
            score += 5
        elif arrowX <= 9 and arrowX >= 1 and arrowY <= 9 and arrowY >= 1:
            score += 1  
        else: pass
        score_text.setText('Your current score: {0}'.format(score))
    win.close
main()
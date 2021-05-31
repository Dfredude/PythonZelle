from graphics import *
def main():
    win = GraphWin('Bouncy', 480, 480)
    win.setCoords(0, 0, 100, 100)

    ball_radius = 10
    ball = Circle(Point(70, 50), ball_radius)
    ball.setFill('blue')
    ball.draw(win)

    dx = 1
    dy = 1
    for i in range(10000):
        ball_center = ball.getCenter()
        ball_centerX = ball_center.getX()
        ball_centerY = ball_center.getY()
        if ball_centerX+ball_radius >=100:
            dx = -1
        if ball_centerX-ball_radius <= 0:
            dx = 1
        if ball_centerY+ball_radius >=100:
            dy = -1
        if ball_centerY-ball_radius <= 0:
            dy = 1 
        ball.move(dx, dy)
        update(30)

    win.getMouse()

main()
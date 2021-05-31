
from graphics import *
from widgets import Button
from Projectile import *

class ShotTracker:
    def __init__(self, win, angle, velocity, height) -> None:
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.draw(win)
    def update(self, dt):
        'Move the shot dt seconds farther along its flight'
        #Update the projectile
        self.proj.update(dt)
        #Move the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx, dy)\
    
    def getX(self):
        return self.proj.getX()
    
    def getY(self):
        return self.proj.getY()

    def undraw(self):
        self.marker.undraw()

class InputDialog:
    '''A custom window for getting simulation values (angle, velocity, and height) from the user'''
    def __init__(self, angle, vel, height) -> None:
        '''Build and display the input window'''
        self.win = win = GraphWin('Initial Values', 480, 480)
        win.setCoords(0, 4.5, 4, .5)

        Text(Point(1, 1), 'Angle').draw(win)
        self.angle = Entry(Point(3, 1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1, 2), 'Velocity').draw(win)
        self.vel = Entry(Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1, 3), 'Height').draw(win)
        self.height = Entry(Point(3, 3), 5).draw(win)
        self.height.setText(str(height))

        self.fire = Button(win, Point(1, 4), 1.25, .5, 'Fire!')
        self.fire.activate()

        self.quit = Button(win, Point(3, 4), 1.25, .5, 'Quit')
        self.quit.activate()

    def interact(self):
        '''Wait for the user to click Quit or Fire button
        Returns a string indicating which button was clicked'''
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt): return 'Quit'
            if self.fire.clicked(pt): return 'Fire!'

    def getValues(self):
        'return input values'
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a, v, h    

    def close(self):
        'close the input window'
        self.win.close()

def main():
    win = GraphWin("Projectile A", 640, 480, autoflush = False)
    win.setCoords(-10, -10, 210, 155)
    Line(Point(-10, 0), Point(210, 0)).draw(win)
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)
    angle, vel, height = 45, 42, 2
    while True:
        inputwin = InputDialog(angle, vel, height)
        choice = inputwin.interact()
        inputwin.close()

        if choice == 'Quit': break

        angle, vel, height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:
            shot.update(1/50)
            update(100)

main()


from random import randrange
from graphics import *
from widgets import Button
from math import degrees, sin, cos, radians

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

class Target:
    def __init__(self, p, radius) -> None:
        self.body = Circle(p, radius)
        self.body.setFill('red')
        self.line1 = Circle(p, radius*.75)
        self.line1.setFill('white')
        self.line2 = Circle(p, radius/3)
        self.line2.setFill('red')

    def draw(self, win):
        self.body.draw(win)
        self.line1.draw(win)
        self.line2.draw(win)

class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2
        self.yvel = yvel1
        print(self.xpos, self.ypos)

    def getY(self): return self.ypos
    
    def getX(self): return self.xpos

class Launcher:

    def __init__(self, win) -> None:
        #Draw the base shot of the launcher
        base = Circle(Point(0,0), 3)
        base.setFill('red')
        base.draw(win)

        #Save the window and create initial angle and velocity
        self.win = win
        self.angle = radians(45)
        self.vel = 40

        #Create initial 'dummy' arrow (needed by redraw)
        self.arrow = Line(Point(0,0), Point(0,0)).draw(win)
        #replace it with the correct arrow
        self.redraw()

    def adjAngle(self, amt):
        '''Create launch angle by amt degrees'''
        self.angle += radians(amt)
        self.redraw()

    def adjVel(self, amt):
        '''Change velocity by amt'''
        self.vel += amt
        self.redraw()
 
    def redraw(self):
        '''Redraw the arrow to show the current angle and velocity'''

        self.arrow.undraw()
        pt2 = Point(self.vel*cos(self.angle), self.vel*sin(self.angle))
        self.arrow = Line(Point(0,0), pt2).draw(self.win)
        self.arrow.setArrow('last')
        self.arrow.setWidth(3)

    def fire(self):
        return ShotTracker(self.win, degrees(self.angle), self.vel, 5)

class ProjectileApp:
    def __init__(self) -> None:
        self.win = GraphWin('Projectile Animation', 720, 480)
        self.win.setCoords(-10, -10, 210, 155)
        Line(Point(0, 0), Point(210, 0)).draw(self.win)
        for x in range(0, 210, 50):
            Text(Point(x, -7), str(x)).draw(self.win)
            Line(Point(x, 0), Point(x, 2)).draw(self.win)
        
        self.launcher = Launcher(self.win)

        self.shots = []

    def run(self):
        while True:
            self.updateShots(1/30)
            key = self.win.checkKey()
            if key in ['q', 'Q']:
                break
            if key == 'Up':
                self.launcher.adjAngle(5)
            elif key == 'Down':
                self.launcher.adjAngle(-5)
            elif key == 'Right': self.launcher.adjVel(5)
            elif key == 'Left': self.launcher.adjVel(-5)
            elif key in ['f', 'F']:
                self.shots.append(self.launcher.fire())
            update(30)
            print(self.shots)

        self.win.close()

    def updateShots(self, dt):
        alive = []
        for shot in self.shots:
            shot.update(dt)
            if shot.getY() >= 0 and -10 < shot.getX() < 210:
                alive.append(shot)
            else:
                shot.undraw()
        self.shots = alive

if __name__ == '__main__': ProjectileApp().run()

from math import sin, cos, radians
from graphics import Circle, Entry, GraphWin, Point, Text

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

def getInputs():
    '''
    a = float(input('Enter the launch angle (in degrees): '))
    v = float(input('Enter the initial velocity (in meters/sec): '))
    h = float(input('Enter the initial height (in meters): '))
    t = float(input('Enter the time interval between position calculations: '))
    '''
    a = 45
    v = 30  
    h = 2
    t = .001
    return a, v, h, t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

from graphics import *

def main():
    #Create graphical Window
    win = GraphWin("Regression line plot", 720, 720)
    win.setCoords(-10, -10, 10, 10)
    #Activate Welcome Screen and initialize variable with data returned from it
    points = welcomeScreen(win)
    #Create regression object
    regressionLine = Regression(win)
    #Add all inputted points to the regressionLine
    for point in points:
        regressionLine.addPoint(point)
    regressionLine.calculateRegressionNDraw()
    #Wait final click
    win.getMouse()


def welcomeScreen(win):
    #Draw instructions message
    message = Text(Point(-5, 8), "Click to delineate points on the graph.")
    message.draw(win)
    #Draw X & Y axis
    axisX = Line(Point(-10,0), Point(10,0))
    axisX.draw(win)
    axisY = Line(Point(0,10), Point(0,-10))
    axisY.draw(win)
    #Draw button Rectangle
    r = Rectangle(Point(-9, -9), Point(-7,-8))
    r.draw(win)
    rCenter = r.getCenter()
    #Draw action button within button rectangle boundaries
    stopMouse = Text(rCenter, "Done")
    stopMouse.draw(win)
    #Accept input from user until <done> button is pressed
    click = Point(0,0)
    points = []
    while True:
        click = win.getMouse()
        if ((-9 <= click.getX() <= -7) and (-9 <= click.getY() <= -8)):
            break
        else:
            #Store user points in an appended list
            points.append(click)
            click.draw(win)
    return points

class Regression:
    def __init__(self, win) -> None:
        self.points = []
        self.win = win
        self.x1, self.x2 = -10, 10
    
    def addPoint(self, point):
        self.points.append(point)

    def predict(self):
        pass

    def calculateRegressionNDraw(self):
        self.__average__()
        regressionLine = Line(Point(self.x1, (self.a + self.b * self.x1)), Point(self.x2, (self.a + self.b * self.x2)))
        regressionLine.draw(self.win)

    def __average__(self):
        sumX = 0
        sumY = 0
        count = 0
        sumXiYi = 0
        sumSqXi = 0
        sumSqYi = 0
        for i in self.points:
            x = i.getX()
            y = i.getY()
            sumX = sumX + x
            sumY = sumY + y
            count = count + 1
            xy = x * y
            sumXiYi = sumXiYi + xy
            SqX = x * x
            sumSqXi = sumSqXi + SqX
            SqY = y * y
            sumSqYi = sumSqYi + SqY

        self.a = ((sumY * sumSqXi) - (sumX * sumXiYi)) / (count * (sumSqXi) - sumX ** 2)
        self.b = ((count * sumXiYi) - (sumX * sumY)) / (count * (sumSqXi) - sumX ** 2)

if __name__ == "__main__": main()
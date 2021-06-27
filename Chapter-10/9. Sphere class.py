from math import pi

class Sphere:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.area = 4*pi*radius**2
        self.volume = 4/3*pi*radius**3

    def getRadius(self):
        return self.radius
    
    def surfaceArea(self):
        return self.area
    
    def volume(self):
        return self.volume
    

def main():
    mySphere = Sphere(5)
    print(mySphere.volume)

main()
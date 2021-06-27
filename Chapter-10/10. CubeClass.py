from math import pi

class Cube:
    def __init__(self, side_length) -> None:
        self.side_length = side_length
        self.surface_area = side_length**2*6
        self.volume = side_length**2*side_length

    def getAwn(self):
        return self.side_length
    
    def surfaceArea(self):
        return self.surface_area
    
    def volume(self):
        return self.volume
    

def main():
    myCube = Cube(5)
    print(myCube.volume)

main()
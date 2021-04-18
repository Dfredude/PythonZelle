import math
def sphereVolume(radius):
    return 4/3*math.pi*(radius**3)

def sphereArea(radius):
    return 4*math.pi*(radius**2)
def main():
    radius = float(input('Enter radius'))
    area = sphereArea(radius)
    volume = sphereVolume(radius)
    print('The Area is ' + str(area) + ' and the Volume is ' + str(volume))

main()
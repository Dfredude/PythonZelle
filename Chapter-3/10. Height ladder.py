import math
height = float(input("Enter the height of the ladder: "))
angle = float(input("Enter the angle of the ladder in degrees: "))
length = height/math.sin(math.radians(angle))
print(length)
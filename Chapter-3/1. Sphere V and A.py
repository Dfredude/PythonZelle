import math
print('This program gets the Volume and Surface Area of a sphere')
radius = eval(input('Enter the radius of the sphere: '))
Volume = 4/3*math.pi*radius**3
Area = 4*math.pi*radius**2
print('The Volume is ', Volume,'and the Area is ', Area)
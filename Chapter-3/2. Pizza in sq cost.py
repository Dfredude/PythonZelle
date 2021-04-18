import math
diameter = eval(input("What is the diameter of your pizza in inches: "))
price = eval(input("What is the price of your pizza: "))
area = math.pi*(diameter/2)**2
cost_per_inch_square = area/price
print('The cost per square inch of your pizza is ', cost_per_inch_square)

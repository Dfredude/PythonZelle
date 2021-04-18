import math

def pizzaArea(diameter):
    radius = diameter/2
    return math.pi*radius**2

def pizzaCostPerSqInch(area, total_cost):
    return total_cost/area

def main():
    diameter = float(input('Enter diameter: '))
    cost = float(input('Enter total cost of pizza: '))
    area = pizzaArea(diameter)
    sq_inch_cost = pizzaCostPerSqInch(area, cost)
    print('Cost per square inch is: ' + str(sq_inch_cost))

main()


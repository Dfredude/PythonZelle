import random as r
def getInput():
    return int(input("Enter the amount of steps to be taken"))

def randomWalk(n):
    place = [0,0]
    x_direction = 'horizontally'
    y_direction = 'vertically'
    for i in range(n):
        place[0] += step()
        place[1] += step()
    if place[0] != 0:
        if place[0] < 0: 
            x_direction = 'backward'
            place[0] = place[0]*-1
        elif place[0] > 0: x_direction = 'forward'
    if place[1] != 0:
        if place[1] < 0:
            y_direction = 'downward'
            place[1] = place[1] * -1
        elif place[1] > 1:
            y_direction = 'upward'
    return place[0], x_direction, place[1], y_direction

def step():
    step = r.randrange(2)
    if step == 0: step = -1
    else: step = 1
    return step

def printOutput(placeX, directionX, placeY, directionY):
    print('Random walk took you {0} steps {1} and {2} {3} from initial place'.format(placeX, directionX, placeY, directionY))

def main():
    n = 50
    placeX, directionX, placeY, directionY = randomWalk(n)
    printOutput(placeX, directionX, placeY, directionY)

main()
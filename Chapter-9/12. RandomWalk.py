import random as r
def getInput():
    return int(input("Enter the amount of steps to be taken"))

def randomWalk(n):
    place = 0
    direction = ''
    for i in range(n):
        place += step()
    if place != 0:
        if place < 0: 
            direction = 'backward'
            place = place*-1
        elif place > 0: direction = 'forward'
    return place, direction

def step():
    step = r.randrange(2)
    if step == 0: step = -1
    else: step = 1
    return step

def printOutput(place, direction):
    print('Random walk took you {0} steps {1} from initial place'.format(place, direction))

def main():
    n = 50
    place, direction = randomWalk(n)
    printOutput(place, direction)

main()
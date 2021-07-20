#One-dimensional random walk (log blocks traveled)
import random as r
def getInput():
    return int(input("Enter the amount of squares that the sidewalk's got: "))

def randomWalk(n):
    squares = [0] * n
    seed = r.randrange(n)
    squares[seed] += 1
    offSidewalk = False
    while not offSidewalk:
        seed += step()
        if seed >= len(squares) or seed < 0: break
        squares[seed] += 1
    return squares



def step():
    return r.randrange(-1, 2, 2)

def printOutput(squares):
    for i in range(len(squares)):
        print('Square {0}: {1}'.format(i, squares[i]))

def main():
    n = 15
    squares = randomWalk(n)
    printOutput(squares)

def test():
    print(step())

if __name__ == '__main__': main()
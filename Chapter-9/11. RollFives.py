import random as r
def rollNtimes(n):
    fives = 0 
    for i in range(n):
        if rollOnce() == 5:
            fives += 1
    return fives

def rollOnce():
    roll = 0
    for i in range(5):
        roll += rollSingleDice()
    return roll

def rollSingleDice():
    return r.randrange(1,7)

def printOutput(result, n):
    print('Probability of getting "5" rolling 5 dices: {0:0.4f}'.format(result/n))

def main():
    n = 5000
    results = rollNtimes(n)
    printOutput(results, n)
    
main()


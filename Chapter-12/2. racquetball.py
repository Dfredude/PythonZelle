from random import random

#Simulate Racquetball Game

def printIntro():
    print('''This program will evaluate the wins among 2 racquetball players in 'n' number of games''')

def getInput():
    probA = float(input('What is the probability player A wins a serve? Valid input =>0 and <1: '))
    probB = float(input('What is the probability player A wins a serve? Valid input =>0 and <1: '))
    n = int(input('How many games to simulate?: '))
    return probA, probB, n

def simNGames(probA, probB, number):
    winsA = winsB = 0
    for game in range(number):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB: winsA += 1
        else: winsB += 1
    return winsA, winsB


def simOneGame(probA, probB):
    scoreA = scoreB = 0
    serve = 'A'
    while not gameOver(scoreA, scoreB):
        if serve == 'A':
            if random() < probA: scoreA += 1
            else: serve = 'B'
        else:
            if random() < probB: scoreB += 1
            else: serve = 'A'
    return scoreA, scoreB 

def gameOver(score1, score2):
    return score1 >= 15 or score2 >= 15

def printOutput(winsA, winsB):
    n = winsA + winsB
    print('Wins for A: {0} ({1:0.1%})'.format(winsA, winsA/n))
    print('Wins for B: {0} ({1:0.1%})'.format(winsB, winsB/n))

def main():
    printIntro()
    probA, probB, n = getInput()
    scoreA, scoreB = simNGames(probA, probB, n)
    printOutput(scoreA, scoreB)

if __name__ == "__main__":
    main()

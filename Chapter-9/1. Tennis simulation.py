from random import random
def printIntro():
    print('''This program will evaluate the wins among 2 tennis players in 'n' number of games''')

def getInput():
    probA = float(input('What is the probability player A wins a serve? Valid input =>0 and <1: '))
    probB = float(input('What is the probability player A wins a serve? Valid input =>0 and <1: '))
    sim_type = str(input('What type of simulation you want a run? single-game, three-games or five-games matches?'))
    n = int(input('How many games to simulate?: '))
    return probA, probB, n, sim_type

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

def simNMatches(probA, probB, number, match_type):
    winsA = winsB = 0
    if match_type == 'three-games' or match_type == 'three games':
        for game in range(number):
            scoreA, scoreB = simMultiGameMatch(probA, probB, 3)
            if scoreA > scoreB: winsA += 1
            else: winsB += 1
    elif match_type == 'five-games' or match_type == 'five games' or match_type == 'Five-games' or match_type == 'Five-Games' or match_type == 'FIVE-GAMES':
        for game in range(number):
            scoreA, scoreB = simMultiGameMatch(probA, probB, 5)
            if scoreA > scoreB: winsA += 1
            else: winsB += 1
    return winsA, winsB

def simMultiGameMatch(probA, probB, n):
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB: winsA += 1
        else: winsB += 1
    return winsA, winsB

def printOutput(winsA, winsB):
    n = winsA + winsB
    print('Wins for A: {0} ({1:0.1%})'.format(winsA, winsA/n))
    print('Wins for B: {0} ({1:0.1%})'.format(winsB, winsB/n))

def main():
    printIntro()
    probA, probB, n , match_type= getInput()
    if match_type == 'single-game' or match_type == 'single game' or match_type == 'SINGLE-GAME':
        winsA, winsB = simNGames(probA, probB, n)
    else:
        winsA, winsB = simNMatches(probA, probB, n, match_type)
    printOutput(winsA, winsB)
main()
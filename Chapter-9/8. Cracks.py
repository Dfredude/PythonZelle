import random as r
def printIntro():
    print('''This program is a simulation of the game cracks''')

def simNGames(n):
    wins = 0
    for i in range(n):
        wins += simOneGame()
    return wins

def simOneGame():
    player_hand = dealer_hand = []
    dealer = player = 0
    while dealer < 17:
        player_handout = handOut()
        dealer_handout = handOut()
        if player_handout[0] > 10:
            player_handout == 10
            
        player_hand.append(player_handout)
        dealer_hand.append(dealer_handout)
        for i in range(len(dealer_hand)):
            dealer += dealer_hand[0]
     

def handOut():
    hand = (r.randrange(1, 13), 0)
    if hand[0] == 1:
        hand[1] == 1
    return hand

def printOutput(result):
    print('You {0}'.format(result))

def main():
    printIntro()
    n = getInput()
    wins = simNGames(n)
    printOutput(wins)

main()


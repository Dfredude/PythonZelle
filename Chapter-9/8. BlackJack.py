import random as r
def printIntro():
    print('''This program is a simulation of the game blackjack and determines de probability of winning the game against the dealer''')

def getInput():
    return int(input('Enter number of games you want to simulate: '))

def simNGames(n):
    wins = 0
    for i in range(n):
        player, dealer = simOneGame()
        if dealer > 21:
            wins += 1
        elif player > dealer and player < 21:
            wins += 1
    return wins

def simOneGame():
    player_hand = []
    dealer_hand = []
    dealer = player = 0
    while dealer < 17:
        dealer = 0
        player_handout = handOut()
        dealer_handout = handOut()
        if player_handout[0] > 10:
            player_handout[0] = 10 
        if player_handout[1] == 1:
            player_handout[0] = 11
        if dealer_handout[0] > 10:
             dealer_handout[0] = 10
        if dealer_handout[1] == 1:
            dealer_handout[1] = 11
        player_hand.append(player_handout)
        dealer_hand.append(dealer_handout)
        for i in dealer_hand:
            dealer += i[0]
        if dealer > 21:
            for i in dealer_hand:
                if i[1] == 1:
                    i[0] = 1
    for card in player_hand:
        player += card[0]
        if player > 21 and card[1] == 1:
                i[0] = 1
                player = 0
                for card in player_hand:
                    player += card[0]
    return player, dealer
     
def handOut():
    hand = [r.randrange(1, 13), 0]
    if hand[0] == 1:
        hand[1] == 1
    return hand

def printOutput(result, n):
    print('Win probability {0}'.format(result/n))

def main():
    printIntro()
    n = getInput()
    wins = simNGames(n)
    printOutput(wins, n)

main()


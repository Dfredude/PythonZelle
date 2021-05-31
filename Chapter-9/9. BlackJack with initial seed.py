import random as r
def printIntro():
    print('''This program is a simulation of the game blackjack and determines de probability of winning the game against the dealer''')

def getInput():
    return int(input('Enter number of games you want to simulate for each initial value: '))

def simNGames(n, initial_value):
    wins = 0
    for i in range(n):
        player, dealer = simOneGame(initial_value)
        if dealer > 21:
            wins += 1
        elif player > dealer and player < 21:
            wins += 1
    return wins

def simOneGame(initial_value):
    player_hand = []
    dealer_hand = []
    if initial_value[0] == 1:
        initial_value[0] = 11
    dealer_hand.append(initial_value)
    player_hand.append(handOut())
    dealer = player = 0
    while dealer < 17:
        dealer = 0
        player_handout = handOut()
        dealer_handout = handOut()
        player_hand.append(player_handout)
        dealer_hand.append(dealer_handout)
        for i in dealer_hand:
            dealer += i[0]
        if dealer > 21:
            for card in dealer_hand:
                if card[1] == 1:
                    card[0] = 1
                    dealer -= 10
    for card in player_hand:
        player += card[0]
    for card in player_hand:    
        if player > 21 and card[1] == 1:
                card[0] = 1
                player -= 10
    print(player_hand, dealer_hand)
    return player, dealer
     
def handOut():
    hand = [r.randrange(1, 13), 0]
    if hand[0] == 1:
        hand[1] = 1
        hand[0] = 11
    elif hand[0] > 10:
        hand[0] = 10
    return hand

def printOutput(result, n):
    for i in range(1, 11):
        print('Win probability for initial seed of {0} to the dealer: {1}'.format(i, result[i-1]/n))

def main():
    printIntro()
    n = getInput()
    wins_for_each_initial_seed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 11):
        hand_out = [i, 0]
        if hand_out[0] == 1:
            hand_out[1] = 1
        wins = simNGames(n, hand_out)
        wins_for_each_initial_seed[i-1] = wins
    printOutput(wins_for_each_initial_seed, n)

main()


import random as r
def printIntro():
    print('''This program is a simulation of the game cracks''')

def rollDoubleDice():
    return rollDice() + rollDice()

def rollDice():
    return r.randrange(1, 7)

def printOutput(result):
    print('You {0}'.format(result))

def cracksGame():
    initial_value = rollDoubleDice()
    if initial_value == 7 or initial_value == 11:
        result = 'win'
    elif 1 > initial_value < 4 or initial_value ==12:
        result = 'lost'
    else:
        roll_for_point_value = rollDoubleDice()
        while roll_for_point_value != initial_value and roll_for_point_value != 7:
            roll_for_point_value = rollDoubleDice()   
        if roll_for_point_value == initial_value: result = 'win'
        elif roll_for_point_value == 7: result = 'lost'
    return result

def main():
    wins = 0
    n = int(input('Enter how many cracks games you want to play: '))
    for game in range(n):
        if cracksGame() == 'win': wins += 1
    print('Probability of wining is ', wins/n)

main()


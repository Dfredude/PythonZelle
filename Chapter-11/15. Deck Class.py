from random import randrange
def shuffle(myList:list):
    taken, newList = myList[:], myList[:]
    length = len(myList)
    for i in range(length):
        taken[i] = ''
    iterations = 0
    for i in range(length):
        correct = False
        while not correct:
            rnum = randrange(0, length)
            if rnum not in taken:
                newList[rnum] = myList[i]
                taken[i] = rnum
                iterations += 1
                correct = True
    myList[:] = newList[:]

def createDeckOfOneSuit(suit:str):
    return [Card(i,suit) for i in range(1, 13)]
        
class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        d_list = ['Ace of diamonds', 'Two of diamonds', 'Three of diamonds', 'Four of diamonds', 
        'Five of diamonds', 'Five of diamonds', 'Six of diamonds', 'Seven of diamonds', 
        'Eight of diamonds', 'Nine of diamonds', 'Jack of diamonds', 'Queen of diamonds',
        'King of diamonds']
        c_list = ['Ace of clubs', 'Two of clubs', 'Three of clubs', 'Four of clubs', 
        'Five of clubs', 'Five of clubs', 'Six of clubs', 'Seven of clubs', 
        'Eight of clubs', 'Nine of clubs', 'Jack of clubs', 'Queen of clubs',
        'King of clubs']
        h_list = ['Ace of hearts', 'Two of hearts', 'Three of hearts', 'Four of hearts', 
        'Five of hearts', 'Five of hearts', 'Six of hearts', 'Seven of hearts', 
        'Eight of hearts', 'Nine of hearts', 'Jack of hearts', 'Queen of hearts',
        'King of hearts']
        s_list = ['Ace of spades', 'Two of spades', 'Three of spades', 'Four of spades', 
        'Five of spades', 'Five of spades', 'Six of spades', 'Seven of spades', 
        'Eight of spades', 'Nine of spades', 'Jack of spades', 'Queen of spades',
        'King of spades']

        if self.suit == 'd':
            return d_list[self.rank-1] 
        elif self.suit == 'c':
            return c_list[self.rank-1]
        elif self.suit == 'h':
            return h_list[self.rank-1]
        else:
            return s_list[self.rank-1]
    
    def getRank(self):
        return self.rank

class Deck:
    def __init__(self) -> None:
        self.cards = createDeckOfOneSuit('c') + createDeckOfOneSuit('d') + createDeckOfOneSuit('h') + createDeckOfOneSuit('s')

    def shuffle(self): shuffle(self.cards)

    def dealCard(self): return self.cards.pop()

    def cardsLeft(self): return len(self.cards)

def main():
    myDeck = Deck()
    for card in myDeck.cards: print(card.getRank(), card.suit)
    myDeck.shuffle()
    for card in myDeck.cards: print(card.getRank(), card.suit)

def test():
    pass
    

if __name__ == '__main__': main()


        
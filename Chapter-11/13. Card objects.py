from os import read, sep
from tkinter.constants import S

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
    
    def getRank(self): return self.rank

    def getSuit(self): return self.suit

def readCards(filename:str) -> list:
    infile = open(filename, 'r')
    cards = []
    for line in infile:
        card_data = line.split(' ')
        print(card_data)
        if len(card_data) > 1:
            cards.append(Card(card_data[0], card_data[1]))
    infile.close()
    return cards

def writeCards(filename:str, cards:list) -> None:
    outfile = open(filename, 'w')
    for card in cards:
        print(str(card.getRank()) + ' ' + str(card.getSuit()), file = outfile)

def main():
    cards = readCards('cards.txt')
    cards.sort(key = Card.getRank, reverse= True)
    for i in cards:
        print(i.getRank(), i.getSuit())
    cards.sort(key = Card.getSuit)
    print()
    for i in cards:
        print(i.getRank(), i.getSuit())
    writeCards('newCards.txt', cards)


main()
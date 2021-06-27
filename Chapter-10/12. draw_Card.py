
from random import randrange
from graphics import *

class Card:
    def __init__(self, rank, suit) -> None:
        if rank <= 10:
            self.rank = str(int(rank)) 
        elif rank == 11: self.rank = 'J'
        elif rank == 12: self.rank = 'Q'
        elif rank == 13: self.rank = 'K'
        print(rank)
        self.suit = str(suit)
        self.short_str = self.rank + 'o' + self.suit

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

    def draw(self, win, center):
        self.image = Image(center, self.short_str + '.png')
        self.image.draw(win)

def main():
    win = GraphWin('Random Cards', 1280, 1280)
    win.setCoords(0,0,10,10)
    suits = ['D','C','H','S']
    x = 2
    for i in range(5):
        myCard = Card(randrange(1,14), suits[randrange(0,4)])
        myCard.draw(win, Point(x, 5))
        x += 1.5
    win.getMouse()

main()
from random import randrange
from graphics import *
from widgets import Button

class Dice:
    def __init__(self) -> None:
        self.dice = [0]*5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1, 7)

    def rollAll(self):
        self.roll(range(5))

    def values(self):
        return self.dice[:]

    def score(self):
        #Create the counts list
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1
        if 5 in counts: return "Five of a kind", 30
        elif 4 in counts: return "Four of a kind", 15
        elif (3 in counts) and (2 in counts): return "Full House", 12
        elif 3 in counts: return "Three of a kind", 8
        elif not (2 in counts) and (counts[1]==0 or counts[6]==0):
            return "Straight", 20
        elif counts.count(2) == 2: return "Two Pairs", 5
        else: return "Garbage", 0

class PokerApp:
    def __init__(self, interface) -> None:
        self.dice = Dice()
        self.money = 100
        self.interface = interface
    
    def intro(self, interface):
        pass

    def run(self):
        while self.money >= 10 and self.interface.wantToPlay(): self.playRound()
        self.interface.close()

    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

class TextInterface:
    def __init__(self) -> None:
        print("Welcome to video poker.")

    def setMoney(self, amt):
        print("You currently have ${0}.".format(amt))
    
    def setDice(self, values):
        print("Dice:", values)

    def wantToPlay(self):
        ans = input("Do you wish to try your luck? ")
        return ans[0] in "yY"

    def close(self):
        print("\nThanks for playing!")
    
    def showResult(self, msg, score):
        print("{0}. You win ${1}.".format(msg, score))

    def chooseDice(self):
        return eval(input("Enter list of which to change ([] to stop) "))

class GraphicsInterface:
    def __init__(self) -> None:
        self.win = GraphWin('Dice Poker', 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300, 30), 'Python Poker Parlor')
        banner.setSize(24)
        banner.setFill('yellow2')
        banner.setStyle('bold')
        banner.draw(self.win)
        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300, 100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300, 170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570, 275), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = Text(Point(300, 325), '$100')
        self.money.setSize(18)
        self.money.draw(self.win)

    def createDice(self, center, size):
        center.move(-3*size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)
        
    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1, 6):
            label = 'Die {0}'.format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)
    
    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))
    
    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)
    
    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])
    
    def chooseDice(self):
        #choices is a list of the indexes of the selected dice
        choices = []
        while True:
            #wait for user to click a valid button
            b = self.choose(['Die 1', 'Die 2', 'Die 3', 'Die 4', 'Die 5', 'Roll Dice', 'Score'])

            if b[0] == "D":
                i = int(b[4]) - 1
                if i in choices:
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:
                for d in self.dice:
                    d.setColor("black")
                if b == "Score":
                    return []
                elif choices != []:
                    return choices

    def choose(self, choices):
        buttons = self.buttons

        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        #get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()

    def setValue(self, value):
        self.value = value
        #Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)

        #Turn the appropiate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)

    def wantToPlay(self):
        ans = self.choose(['Roll Dice', 'Quit'])
        self.msg.setText("")
        return ans == "Roll Dice"

    def close(self):
        self.win.close()

class Intro:
    def __init__(self) -> None:
        self.win = GraphWin('Intro', 600, 400)
        self.intro_msg = Text(Point(300, 300), '''This is a Dice Poker Game.
        Press the help button at anytime for help''').draw(self.win)
        self.LetsPlayB = Button(self.win, Point(300, 200), 70, 30, "Let's play")
        self.LetsPlayB.activate()
        self.quitB = Button(self.win, Point(500, 350), 50, 30, "Quit")
        self.quitB.activate()

    def run(self):
        while True:
            click = self.win.getMouse()
            if self.LetsPlayB.clicked(click): break
            elif self.quitB.clicked(click): return 'Quit'
        self.removeIntro()

    def removeIntro(self):
        self.intro_msg.undraw()
        self.LetsPlayB.deactivate()
        self.LetsPlayB.undraw()

class DieView:
    'Widget that displays a graphical representation of a dice'
    def __init__(self, win, center, size) -> None:
        'Create a view of a die, e.g.: d1 = DieView(mywin, Point(40,50), 20)'
        self.win = win
        self.background = 'white' #color of die face
        self.foreground = 'black' #color of the pips
        self.psize = 0.1 * size
        hsize = size/2
        offset = 0.6 * hsize

        #create square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        #Create 7 circles for standard pip locations
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)

    def __makePip(self, x, y):
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        'Set this die to display value'
        self.value = value
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        
    def setColor(self, color):
        'Sets the color of the dice'
        self.foreground = str(color)
        value = self.value
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)

class MSDice:
    def __init__(self, sides) -> None:
        self.sides = sides
        self.value = 1
    
    def roll(self):
        self.value = randrange(1, self.sides+1)

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

if __name__ == '__main__':
    intro = Intro()
    if intro.run() != 'Quit':
        inter = GraphicsInterface()
        app = PokerApp(inter)
        app.run()
from random import randrange

class Interface:
    def __init__(self) -> None:
        pass

    def displayShooterRoll(self, value):
        print('Shooter rolled a ', value)

    def disWinner(self, winner):
        print(winner, ' Won the round')

    def disMoney(self, p1, p1_money, p2, p2_money):
        print("{0}'s got ${1}, {2}'s got ${3}".format(p1, p1_money, p2, p2_money))

    def getNames(self):
        n1 = str(input('Enter your name, player 1: '))
        n2 = str(input('Enter your name, player 2: '))
        return n1, n2

    def getBet(self, player):
        return int(input('How much are you going to bet {0}? '.format(player.getName())))

    def getMatchOrFade(self, player):
        m_o_f = str(input('{0}, do you wish to match or fade? '.format(player.getName())))
        if m_o_f[0].lower() == 'm': return 0
        elif m_o_f[0].lower() == 'f': return int(input('How much?'))

    def getContinueDecision(self):
        return str(input('Do you wish to play again? Y/N: '))

class craps:
    def __init__(self, interface) -> None:
        self.interface = interface
        p1_name, p2_name = self.whoIsGonnaPlay()
        self.player1 = Player(p1_name)
        self.player2 = Player(p2_name)

    def whoIsGonnaPlay(self):
        name1, name2 = self.interface.getNames()
        return name1, name2

    def playGame(self):
        gameOn = True
        while gameOn:
            winner = self.playRound()
            self.interface.disWinner(winner.getName)
            self.interface.disMoney(self.player1.getName(), self.player1.money, 
            self.player2.getName(), self.player2.money)
            decision = self.interface.getContinueDecision()
            if decision[0].lower() == 'N': gameOn = False

    def playRound(self):
        shooter, non_shooter = self.selectShooter()
        bet = self.interface.getBet(shooter)
        match_or_fade = self.interface.getMatchOrFade(non_shooter)
        if match_or_fade > bet: bet = match_or_fade
        shooter.roll()
        if shooter.getValue() == 7 or shooter.getValue() == 11:
            self.interface.displayShooterRoll(shooter.getValue()) 
            shooter.setStatus('win')
        elif shooter.getValue() == 2 or shooter.getValue() == 3 or shooter.getValue() == 12:
            self.interface.displayShooterRoll(shooter.getValue())
            shooter.setStatus('loss')
        else:
            p = shooter.getValue()
            print(p)
            point_game = True
            while point_game == True:
                shooter.roll()
                self.interface.displayShooterRoll(shooter.getValue())
                if shooter.getValue() == p:
                    point_game = False 
                    shooter.setStatus('win')
                elif shooter.getValue() == 7: 
                    point_game = False
                    shooter.setStatus('loss')

        if shooter.getStatus() == 'win': 
            shooter.money += bet
            non_shooter.money -= bet
            return shooter
        else: 
            non_shooter.money += bet
            shooter.money -= bet
            return non_shooter

    def selectShooter(self):
        shooter = False
        while shooter == False:
            self.player1.roll()
            self.player2.roll()
            if self.player1.getValue() > self.player2.getValue():
                shooter = self.player1
                non_shooter = self.player2
            elif self.player2.getValue() > self.player1.getValue():
                shooter = self.player2
                non_shooter = self.player1
        print(shooter.getName(), ' is the shooter!')
        return shooter, non_shooter

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.money = 100

    def roll(self):
        self.value = randrange(1, 13)

    def setStatus(self, status:str):
        self.status = status

    def getValue(self):
        return self.value
    
    def getName(self):
        return self.name

    def getStatus(self):
        return self.status

crapsGame = craps(Interface())
crapsGame.playGame()
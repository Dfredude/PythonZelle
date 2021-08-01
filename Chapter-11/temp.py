class chef:
    def __init__(self, specialDish:str) -> None:
        self.specialDish = specialDish
        self.salad = 'Cesar Salad'

    def makeSpecialDIsh(self): print('Here is your ', self.specialDish)

    def makeSalad(self): print('Here is your {0}'.format(self.salad))

class mexicanChef(chef):
    def __init__(self) -> None:
        super().__init__('Taco')
        

myChef = chef('Biscuit')
myMChef = mexicanChef()

myChef.makeSpecialDIsh()
myMChef.makeSpecialDIsh()
myChef.makeSalad()
myMChef.makeSalad()

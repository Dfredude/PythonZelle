import json
from math import pi

class ATM:
    def __init__(self, interface) -> None:
        self.users = self.readUsers()
        self.interface = interface

    def readUsers(self):
        infile = open('Chapter-12/ATM-Users.json', 'r')
        instr = infile.read()
        users = json.loads(instr)
        infile.close()
        return users

    def writeStudents(self):
        outfile = open('Chapter-12/ATM-Users.json', 'w').read()
        outjs = json.dumps(self.users)
        print(outjs, outfile)
        outfile.close()

    def checkMoney(self, id, account):
        for user in self.users['users']:
            if user['ID'] == id:
                return user[account]

    def transferMoney(self, id, account, amt):
        index = self.interface.options2.index(account)
        if index == 0: to_account = 'savings'
        else: to_account = 'checking'
        for user in self.users['users']:
            if user['ID'] == id:
                user[account] - amt
                user[to_account] + amt
    
    def withdrawMoney(self, id, account, amt):
        for user in self.users['users']:
            if user['ID'] == id:
                user[account] - amt

    def checkLogIn(self, id, pin):
        for user in self.users['users']:
                if user['ID'] == id and user['PIN'] == pin:
                    return True

    def run(self):
        if self.interface.scene1() == 'log in':
            logIn = False
            while logIn == False:
                id, pin = self.interface.logInScene()
                if self.checkLogIn(id, pin) == True: logIn = True
                else: print('Wrong ID or PIN, please try again.')
            run = True
            while run == True:
                account = self.interface.scene3()
                operation = self.interface.scene4()
                if operation == 'check': 
                    money = self.checkMoney(id, account)
                    print('You got {0}'.format(money))
                elif operation == 'withdraw':
                    amt = self.interface.scene5()
                    self.withdrawMoney(id, account, amt)
                    print('Operation Succesfull')
                else: 
                    amt = self.interface.scene5()
                    self.transferMoney(id, account, amt )
                    print('Operation Succesfull')
                cmd = input('Do you wish to do another operation? (Y/N): ')
                if cmd[0].lower() == 'n': run = False


                

class ATMInterface():
    def __init__(self) -> None:
        self.options1 = ['log in', 'exit']
        self.options2 = ['checking', 'savings']
        self.options3 = ['check', 'withdraw', 'transfer']
    
    def scene1(self):
        cmd = str(input('Enter a command (log in, exit): '))
        while cmd.lower() not in self.options1:
            cmd = str(input('Enter a command (log in, exit): '))
        return cmd
    
    def logInScene(self):
        id = str(input('Enter your User ID: '))
        pin = str(input('Enter your PIN: '))
        return id, pin

    def scene3(self):
        account = str(input('Enter an account (checking, savings): '))
        while account.lower() not in self.options2:
            account = str(input('Enter an account (checking, savings): '))
        return account

    def scene4(self):
        cmd = str(input('Enter an operation (check, withdraw, transfer): '))
        while cmd not in self.options3:
            cmd = str(input('Enter an operation (check, withdraw, transfer): '))
        return cmd

    def scene5(self):
        return float(input('How much?: '))


        

    


ATM(ATMInterface()).run()
from math import *

def main():
    num = int(input('Enter a number to chek if it is prime: '))
    prime = True
    if num > 2:
        for i in range(2, round(sqrt(num))):
            if num % i == 0:
                print('Not prime')
                prime = False
        if prime == True:
            print('The number is prime')
        else:
            print('The number is not prime')
main()
from math import *

def guess(number, iterations, initial_guess):
    guess = 0
    for i in range(iterations):
        guess = (guess+number/initial_guess)/2
    difference = sqrt(number)-guess
    return guess, difference

number = float(input("Enter the number whose suare root you'd like to know: "))
iterations = int(input("Enter the number of times Newton's method should iterate: "))
initial_guess = float(input("Enter your initial guess of what the square root may be: "))
guess, difference = guess(number, iterations, initial_guess)
print('The result is: {0:0.2f} and their was an error of {1:0.2f} in respect to the python function'.format(guess, difference))

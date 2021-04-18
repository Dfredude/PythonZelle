import math
def guess(number, iterations, initial_guess):
    for i in range(iterations):
        guess = (guess+number/initial_guess)/2
    difference = math.sqrt(number)-guess
    return guess, difference
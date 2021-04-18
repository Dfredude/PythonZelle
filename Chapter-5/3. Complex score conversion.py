from math import *

def main():
    #Get score input
    score = int(input('Score from 0 to 100: '))
    #Create list of values
    grades = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A']
    if score < 60:
        nscore = 0
    if 90 > score > 60:
        score = score/10
        nscore = int(floor(score))
    if 100 >= score > 89:
        nscore = 9
    print('The grade is {0}'.format(grades[nscore]))
    
main()
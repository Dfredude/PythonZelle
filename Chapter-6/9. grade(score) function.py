from math import *
def grade(score):
    grades = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A']
    if score < 60:
        nscore = 0
    elif 90 > score > 60:
        score = score/10
        nscore = int(floor(score))
    elif 100 >= score > 89:
        nscore = 9
    return grades[nscore]

def main():
    #Get score input
    score = int(input('Score from 0 to 100: '))
    #Get score
    nscore = grade(score)
    print('The grade is {0}'.format(nscore))
    
main()
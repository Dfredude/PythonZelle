from math import *

def main():
    #Get string input
    names = str(input('Enter a value to convert to its acronym: ')).split()
    #Loop through each word and get index value 0
    acronym = ''
    for i in names:
        acronym += i[0]
    #Upper
    upper_acronym = acronym.upper()
    print('The acronym is {0}'.format(upper_acronym))
main()
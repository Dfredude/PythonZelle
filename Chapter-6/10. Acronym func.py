from math import *
def acronym(words):
    acronym = ''
    for i in words.split():
        acronym += i[0]
    return acronym.upper()

def main():
    #Get string input
    names = str(input('Enter a value to convert to its acronym: '))
    #Loop through each word and get index value 0
    upper_acronym = acronym(names)
    print('The acronym is {0}'.format(upper_acronym))
main()
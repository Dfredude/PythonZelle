def main():
    #Get score inout
    Score = int(input('Score from 0 to 5: '))
    #Create List of grades to later on use them by indexing the input
    grades = ['F', 'F', 'D', 'C', 'B', 'A']
    #Print using slots in a string
    print('The converted grade is: {0}'.format(grades[Score])) # We are getting the proper grade using list index

main()
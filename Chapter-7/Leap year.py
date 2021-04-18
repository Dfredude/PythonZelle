def main(): 
    year = int(input('Enter year: '))
    if year % 400 != 0:
        leap_year = 0
    else:
        if year % 4 == 0:
            leap_year = 1
        else:
            leap_year = 0
    boolean = ['isn\'t', 'is']
    print('The year {0}, {1} a leap year'.format(year, boolean[leap_year] ))

main()
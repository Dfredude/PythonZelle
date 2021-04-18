def main():
    year = int(input('Enter year: '))
    if year >= 1900 and year <=2099:
        a,b,c = year%19, year%4, year%7 
        d = (19*a + 24) % 30
        e = (2*b + 4*c + 6*d + 5) % 7
        easter = 21 + d + e
        if year == 1954 or year == 1981 or year == 2049 or year ==2076:
            easter = easter - 7
        #Create months
        march = []
        april = []
        for i in range(22, 32):
            march.append(i)
        for i in range(1, 31):
            april.append(i)
        #March or April
        if easter >31:
            day = april[easter-31]
            month = 'April'
        else:
            day = march[easter-22]
            month = 'March'
        print('Easter day in year {0} will be {1} {2}'.format(year, month, day))
    else:
        print('Sorry!, the year entered is out of our boundaries to calculate')

main()
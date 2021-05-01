def leapYear(year):
    if year % 400 != 0:
        leap_year = 0
    else:
        if year % 4 == 0:
            leap_year = 1
        else:
            leap_year = 0
    return leap_year
    
def main():
    #This is a simple program I made. I think in simple programs it doesn't matter much, but in larger and complex ones avoiding a lot of nesting would be nicer to have. I wonder whether I'm right or not.
    date = str(input('Enter a date in mm/dd/yyyy format: ')) #Input date from user
    date_values = date.split('/') #Split the values
    #Initialize each of the values
    month = int(date_values[0])
    day = int(date_values[1])
    year = int(date_values[2])
    validation = False
    #Create List that determines the number of days of each month
    days_in_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #Acept only year from 1900 through 2099
    if year >= 1900 and year <= 2099:
        #Determine if year is a leap year (Returns boolean value)
        leap_year = leapYear(year)
        #Add one day to february in case we deal with a leap year
        if leap_year == 1:
            days_in_each_month[1] += 1
        #Validate month
        if month > 0 and month < 13:
            #Validate month's day
            if day <= days_in_each_month[month-1] and day >= 1:
                #Return true value
                validation = True
    boolean = ['invalid', 'valid'] #Two posible outputs in the list
    #Output validation
    print('The date is {0}'.format(boolean[validation]))

main()


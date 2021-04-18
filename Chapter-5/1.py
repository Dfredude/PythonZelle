def main():
    dateStr = str(input('Enter date (mm/dd/yyyy):'))
    monthStr, daysStr, yearStr = dateStr.split('/')
    monthInt = int(monthStr)-1
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December']
    print('The converted date is: {0} {1}, {2}'.format(months[monthInt], daysStr, yearStr))
main()
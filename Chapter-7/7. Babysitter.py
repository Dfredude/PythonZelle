def minuteToDecimal(minutes):
    return minutes/60

def timeFormatToInts(time):
    hour_string = ''
    min_string = ''
    for i in range(len(time)-3):
        if time[i] != ' ' and time[i] != ':':
            hour_string += time[i]
            last_iteration = i
    for j in time[last_iteration+2:]:
        min_string += j
    return int(hour_string), int(min_string)

def main():
    #Get input
    print('This program computes the pay fora babysitting shift only within one day (0-24 hrs).')
    start_time = str(input('Enter the starting time in hh:mm format: '))
    off_time = str(input('Enter the time you got off babysitting: '))
    #Convert hour to int, minute to int of both time formats
    start_hour, start_min = timeFormatToInts(start_time)
    off_hour, off_min = timeFormatToInts(off_time)
    # Turn minutes to decimals
    start_min_decimal = start_min/60
    off_min_decimal = off_min/60
    #Set low paid hours to 0 by defualt
    low_paid_total = 0
    #Detect if off time passes or is equal to 9:00 PM
    if off_hour >= 21:
        #Determine low paid hours pay
        low_paid_hours_pay = (off_hour - 21) * 1.75
        #Determine low paid minutes pay
        low_paid_minutes_pay = off_min_decimal * 1.75
        low_paid_total = low_paid_hours_pay + low_paid_minutes_pay
        off_hour = 21
        off_min_decimal = 0
    normal_paid_total = (off_hour + off_min_decimal - start_hour - start_min_decimal) * 2.5
    total_pay = normal_paid_total + low_paid_total
    print(normal_paid_total, low_paid_total)
    print('Your pay is ${0}'.format(total_pay))

main()
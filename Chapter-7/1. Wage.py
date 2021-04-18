def main():

    hrs_worked = float(input('How many hours did you work: '))
    normal_wage = float(input('What is your normal hourly wage: '))
    extra_hrs = 0
    if hrs_worked > 40:
        extra_hrs = hrs_worked - 40 
    pay = (hrs_worked - extra_hrs  ) * normal_wage + (extra_hrs * 1.5 * normal_wage)
    print('Your wage this week is ${0:0.2f}'.format(pay))

main()
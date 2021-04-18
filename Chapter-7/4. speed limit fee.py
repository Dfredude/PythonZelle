def main():
    clock_speed = float(input('What\'s the speed?: '))
    speed_limit = int(input('Enter speed limit: '))
    if clock_speed <= speed_limit:
        print('Have a great day!')
    else:
        dif = clock_speed - speed_limit
        cost_of_extra_mph = dif * 5
        if clock_speed > 90:
            over_ninety_fine = 200
            total_cost = 50+over_ninety_fine+cost_of_extra_mph
        else:
            total_cost = 50 + cost_of_extra_mph
        print('''You surpassed the speed limit by {0:0.2f} mph and the total fine is ${1}.
Over speed limit fine: $50
Fine per each mile surpassed: ${2:0.2f}
Fine for surpassing the federal limit of 90mph: ${3:0.2f}'''.format(dif, total_cost, cost_of_extra_mph, over_ninety_fine))

main()
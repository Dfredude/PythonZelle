def main():
    odometer = int(input('Enter starting odometer reading: '))
    current_odometer = True
    gas_used = True
    all_legs_current_odometer = []
    all_legs_gas_used = []
    while bool(current_odometer) != False or bool(gas_used) != False:
        current_odometer = str(input('Enter next leg odometer reading: '))
        if bool(current_odometer) == False:
            break
        gas_used = str(input('Enter gas used in this leg: '))
        if bool(gas_used) == False:
            break
        all_legs_current_odometer.append(int(current_odometer))
        all_legs_gas_used.append(int(gas_used))
    print(all_legs_current_odometer, all_legs_gas_used)

    legs_mph = []
    for i in range(len(all_legs_current_odometer)):
        legs_mph.append((all_legs_current_odometer[i]-odometer)/all_legs_gas_used[i])
        odometer = all_legs_current_odometer[i]

    for i in range(len(legs_mph)):
        result = 'No. ' + str(i+1) + ' leg had: ' + '{0:0.2f} mpg'.format(legs_mph[i])
        print(result)

    print('The total trip mpg was: ' + str(sum(legs_mph)/len(legs_mph)))
main()



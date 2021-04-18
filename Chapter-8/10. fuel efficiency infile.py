def main():
    #Input file
    infile = open('legs_info.txt', 'r')
    odometer = int(infile.readline())
    current_odometer = ''
    gas_used = ''
    all_legs_info = infile.readlines()
    all_legs_current_odometer = []
    all_legs_gas_used = []
    for i in range(len(all_legs_info)):
        current_odometer, gas_used = all_legs_info[i].split(',')
        all_legs_current_odometer.append(int(current_odometer))
        all_legs_gas_used.append(int(gas_used))
    legs_mph = []
    for i in range(len(all_legs_current_odometer)):
        legs_mph.append((all_legs_current_odometer[i]-odometer)/all_legs_gas_used[i])
        odometer = all_legs_current_odometer[i]

    for i in range(len(legs_mph)):
        result = 'No. ' + str(i+1) + ' leg had: ' + '{0:0.2f} mpg'.format(legs_mph[i])
        print(result)

    print('The total trip mpg was: ' + '{0:0.2f}'.format(sum(legs_mph)/len(legs_mph)))
main()



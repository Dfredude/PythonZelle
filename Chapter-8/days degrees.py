def tempDay(average_temp):
    average_temp = int(average_temp)
    if average_temp < 60:
        day = 'cool'
        degrees = 60 - average_temp
    elif average_temp > 80:
        day = 'heat'
        degrees = average_temp - 80
    else:
        day = 'normal'
        degrees = False
    return day, degrees

def main():
    infile = open('degrees.txt', 'r')
    day = infile.readline()
    heat_degrees = 0
    heat_days = 0
    cool_degrees = 0
    cool_days = 0

    while bool(day) == True:
        if bool(day) == False:
            break
        dayResult, degrees = tempDay(int(day)) 
        if dayResult == 'heat':
            heat_days += 1
            heat_degrees += degrees
        elif dayResult == 'cool':
            cool_days += 1
            cool_degrees += degrees
        day = infile.readline()
        print(day)
        
    print('There were {0} hot days consisting of a total {1} degrees over average and {2} cold days consisting of a total {3} degrees below'.format(heat_days, heat_degrees, cool_days, cool_degrees))
main()



        
def windchill(T,V):
    return 35.74 + 0.6215*T - 35.75*V**0.16 + 0.4275 *T*V*0.16
def main():
    row_values = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    column_values = [-20, -10, 0, 10, 20, 30, 40, 50, 60]

    complete_column_string = ' '
    for temperature in column_values:
        column_string = '{0:<7}'.format(temperature)
        complete_column_string = complete_column_string + ' ' + column_string
    print('  ' + complete_column_string)        
    
    for velocity in row_values:
        if velocity > 3:
            velocity_str = '{0:2}'.format(velocity)
            row_results_string = ''
            for temperature in column_values:
                result = windchill(temperature, velocity)
                result_string = '{0:<7.1f}'.format(result)
                row_results_string = row_results_string + ' ' + result_string 
            row_results_string = velocity_str + ' ' + row_results_string    
            print(row_results_string)

main()

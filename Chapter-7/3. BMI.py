def main():
    height = float(input('Enter your height in inches: '))
    mass = float(input('Enter your mass in inches: '))
    BMI = mass * 720 / height**2
    if BMI > 25:
        status = 'overweight'
    elif BMI < 19:
        status = 'way too thin'
    else:
        status = 'healthy'       
    print('BMI is {0:0.2f}, so you\'re {1}'.format(BMI, status))

main()
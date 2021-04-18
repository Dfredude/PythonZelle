def main():
    age = int(input('Enter your age: '))
    citizenship = int(input('Enter the amount of years you\'ve been US citizen: '))
    if age >= 25 and citizenship >= 7:
        if age >=30 and citizenship >= 9:
            print('Congratulation you are eligible for becoming US representetive or US senator!.')
        else:
            print('Congratulation you are eligible for becoming US representetive!.')
    else:
        print('Sorry!, you are not eligible for becoming US representetive nor US senator.')

main()
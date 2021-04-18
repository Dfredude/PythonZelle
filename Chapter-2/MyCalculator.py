def main():
    print('This program solves simple mathematical expressions')
    for i in range(100):
        Expression = eval(input('Enter any mathematical expression(* to multiply,/ to divide,** to power): '))
        print('The answer is',Expression)
main()
    
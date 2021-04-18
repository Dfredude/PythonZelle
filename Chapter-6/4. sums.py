def sumNatNumb(n):
    j = 0
    for i in range(1, n+1):
        j += i
    return j

def sumCubes(n):
    j = 0
    for i in range(1, n+1):
        j += i**3
    return j

def main():
    n = int(input('Enter a number'))
    print('Sum of natural numbers: ' + str(sumNatNumb(n)) + ' Sum of natural cubed numbers is: ' + str(sumCubes(n)))

main()

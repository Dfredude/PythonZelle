def main():
    num = int(input('Enter a number: '))
    iteration = 0
    while num % 2 > 0:
        print(num)
        num = num*3 +1
        iteration += 1
    while num >1:
        print(num)
        num //= 2
        iteration += 1
    print('{0} iterations to finally get 1 as output'.format(iteration))

main()
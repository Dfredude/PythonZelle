def main():
    m, n = (str(input('Enter m, n: '))).split(',')
    m, n = int(m), int(n)
    while m != 0:
        n, m = m, n%m
    GCD = n
    print('The GCD is {0}'.format(GCD))

main()
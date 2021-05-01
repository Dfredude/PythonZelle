def main():
    inves_perm = float((input('Enter initial investment: ')))
    year_rate = int(input('Enter the yearly interest rate in percentage: '))/100
    inves_var = inves_perm
    year = 0
    print(year_rate)
    while inves_var < inves_perm*2:
        inves_var = inves_var + inves_var*year_rate
        year += 1
    print('Your investment returns in {0} years with a total of ${1:0.2f}'.format(year, inves_var))
main()
def main():
    print("This program calculates the future value\n", "of a n-year(s) investment.")
    #principal = float(input("Enter the initial principal: "))
    #apr = float(input("Enter the annual interest rate: "))
    #years = int(input('For how many years?: '))
    principal = 1000
    apr = .1
    years = 10

    print("{0:^6} {1:^11}".format("Year", "Value"))
    print("----------------------")

    for i in range (years):
        principal = principal * (1 + .01 * apr)
        print("{0:^6}   ${1:<}.{2:0^2}".format(i+1, int(principal), int(principal%1 * 100)))

main()
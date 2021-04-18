def main():
    credits = int(input('How many credits do you have?: '))
    if credits < 26:
        standing = 'Junior'
        if credits < 16:
            standing = 'Sophomore'
            if credits < 7:
                standing = 'Freshman'
    else:
        standing = 'Senior'
    print('Your standing is {0}'.format(standing))

main()
    
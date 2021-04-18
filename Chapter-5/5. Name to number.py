def main():
    #Get string input
    name = str(input('Enter a single name to get its value: '))
    print(name)
    #Loop through each letter of the name and add value
    value = 0
    for i in name:
        j = ord(i.upper()) - 64
        value += j
    #Output
    print('The value of your name is {0}'.format(value))
main()
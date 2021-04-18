def main():
    #Get full name string input
    full_name = str(input('Enter full name to get its value: ')).split()
    #Loop through each letter of the name and add value
    value = 0
    for i in full_name:
        for j in i:
            k = ord(j.upper()) - 64
            value += k
    #Output
    print('The value of your name is {0}'.format(value))
main()
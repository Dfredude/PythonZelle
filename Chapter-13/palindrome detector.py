def main():
    inputted_string = str(input("Enter a word or sentence: "))
    reversed_string = inputted_string[::-1]
    print(inputted_string, reversed_string)
    palindrome = True
    for i in range(len(inputted_string)):
        if inputted_string[i] != reversed_string[i]:
            palindrome = False
    if palindrome == True:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome, lol")

if __name__ == "__main__":
    main()

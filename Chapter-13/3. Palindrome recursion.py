def isPalindrome(inputString):
    if len(inputString) >= 2:
        if inputString[0] == inputString[-1]:
            return isPalindrome(inputString[1:-1])
        else: return False
    else:
        return True

def main():
    inputted_string = str(input("Enter a word or sentence: "))
    if isPalindrome(inputted_string):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome, lol")

if __name__ == "__main__":
    main()

def main():

#Get plaintext(p_text) and key(x) from the user
    p_text = str(input("Enter the message you'd like encrypted:\n"))
    key = int(input("What's the key?: "))
    p_text = p_text.upper()
    
#Create string of letters
    table = "abcdefghijklmnopqrstuvwxyz"
    full_table = table * 6
#Check if there are spaces
#Convert plaintext to ciphertext(c_text) using cipher loop
    result = ""
    for ch in p_text:
        if ch == ' ':
            result += ' '
        else:
            new_n = ord(ch) + 13
            result += full_table[new_n+key]
    print("Your encoded message is {0}.".format(result))

main()
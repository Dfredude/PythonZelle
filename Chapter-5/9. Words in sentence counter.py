def main():
    #Get string sentence
    sentence = str(input("Enter the sentence to count its letters:\n"))
    #Initialize variable to store data 
    j = 0 
    #Loop
    for i in sentence.split():
        j += 1
    print("The number of words are {0}.".format(j))

main()
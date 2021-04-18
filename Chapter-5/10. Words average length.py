def main():
    #Get string sentence
    sentence = str(input("Enter the sentence to count its letters:\n"))
    #Initialize variable to store data 
    total = 0
    words = sentence.split()
    #Loop
    for i in words:
        length = len(i)
        total += length
    number_of_words = len(words)
    average_word_length = total/number_of_words
    print("The average word length is {0}.".format(average_word_length))

main()
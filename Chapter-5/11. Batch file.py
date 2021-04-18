def main():
    #Get string sentence from a file
    file_name = input('Enter filename: ')
    infile = open(file_name, "r")
    data = infile.read()
    #Initialize variable to store data 
    total = 0
    words = data.split()
    #Loop
    for i in data.split():
        length = len(i)
        total += length
    number_of_words = len(words)
    average_word_length = total/number_of_words
    print("The average word length is {0}.".format(average_word_length))

main()
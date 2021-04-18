def main():
    #Get string sentence from a file
    file_name = input('Enter filename: ')
    infile = open(file_name, "r")
    data = infile.read()
    words = data.split()
    #Loop
    number_of_words = len(words)
    print("There are {0} words in this file.".format(number_of_words))

main()
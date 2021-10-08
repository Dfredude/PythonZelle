import json

def main():
    printIntro()
    dictionary = readDictionary()
    #Converting the text input into a list of words
    infile = readFile("Chapter-13\sample.txt")
    checkSpelling(infile, dictionary)
    printOutro()
    

def printIntro():
    print("Welcome to this program that detects mispelling in text documents.", "Processing..." ,sep="\n")

def readDictionary():
    infile = open("Chapter-13\\words_dictionary.json", 'r')
    dic_string = infile.read()
    loaded_json = json.loads(dic_string)
    infile.close()
    return loaded_json

def readFile(text):
    file = open(text, 'r')
    wholetext = file.read()
    #Remove symbols/none-words
    wordsOnlyText = getOnlyWords(wholetext)
    file.close()
    return wordsOnlyText.split()

def getOnlyWords(text:str):
    newString = ""
    for i in range(len(text)):
        if text[i].isalpha() or text[i] == ' ' or text[i] == "'":
            newString += text[i]
    return newString

def checkSpelling(words:list, dictionary):
    for word in words:
        if not (word.lower() in dictionary):
            print("Potentially incorrect word found: ", word)

def printOutro():
    print("Program's finished.")

if __name__ == "__main__": main()

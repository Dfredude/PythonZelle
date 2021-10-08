from anagram_algorithm import getAnagrams
import json

def main():
    word = getInput()
    dic = getDictionary("Chapter-13\words_dictionary.json")
    result = isValidAnagram(word, dic)
    printResult(result)

def getInput():
    print("""This program returns an anagram if it's another word""")
    return str(input("Please enter a word: "))

def getDictionary(file):
    infile = open(file, 'r')
    allText = infile.read()
    convertedText = json.loads(allText)
    infile.close()
    return convertedText

def getOnlyWords(text:str):
    newString = ""
    for i in range(len(text)):
        if text[i].isalpha() or text[i] == ' ' or text[i] == "'":
            newString += text[i]
    return newString

def isValidAnagram(word:str, dictionary):
    word = word.lower()
    rslt = False
    anagrams = getAnagrams(word)
    for anagram in anagrams:
        anagraml = anagram.lower()
        if ((anagraml in dictionary) and (anagraml != word)):
            print("Hey! Here is a new word made out of your word; ", anagram)
            rslt = True
    return rslt

def printResult(result):
    if result:
        print("Congrats! You entered a word with one or more anagrams that creae new words.")
    else:
        print("Sorry, your word doesn't output any new word out of its anagrams.")


if __name__ == "__main__": main()



def censor(text:str, censor_words:list):
    words = text.split(' ')
    punctuation_marks = [',', '.', '!', '?']
    for i in range(len(words)):
        count = 0
        spec_character = False
        for j in words[i]:
            count += 1
            if j in punctuation_marks:
                spec_character = True
                count -= 1
        if words[i] in censor_words or words[i][:-1] in censor_words:
            newWord = '*' * count 
            if spec_character == True: 
                newWord += words[i][-1:]
            words[i] = newWord
            print(newWord)
    newText = ''
    for word in words:
        newText = newText + ' ' + word
    return newText    

def main():
    infile = open('text.txt', 'r')
    text = infile.read()
    infile.close()
    print(text)
    new_text = censor(text, ['brother', 'luck', 'wish', 'army'])
    outfile = open('censored.txt', 'w')
    print(new_text, file = outfile)
    print(new_text)
    outfile.close()

if __name__ == '__main__': main()
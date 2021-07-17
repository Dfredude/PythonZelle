def censor(text:str):
    words = text.split(' ')
    punctuation_marks = [',', '.', '!', '?']
    for i in range(len(words)):
        count = 0
        spec_character = False
        for j in words[i]:
            if j not in punctuation_marks:
                count += 1
            else:
                spec_character = True
        if count == 4:
            newWord = '****' 
            if spec_character == True: newWord += words[i][-1:]
            words[i] = newWord
    newText = ''
    for word in words:
        newText = newText + ' ' + word
    return newText    


def main():
    infile = open('text.txt', 'r')
    text = infile.read()
    infile.close()
    print(text)
    new_text = censor(text)
    outfile = open('censored.txt', 'w')
    print(new_text, file = outfile)
    
    outfile.close()

if __name__ == '__main__': main()
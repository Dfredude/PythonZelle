
def removeDuplicates(myList):
    length = len(myList)
    duplicated_numbers = 0
    for i in range(length):
        for j in range(1, length):
            if myList[i] == myList[j] and myList[j] != '`' and i != j:
                myList[j] = '`'
                duplicated_numbers += 1
    newList = myList[:-duplicated_numbers]
    positions = 0
    for i in range(length):
        if myList[i] != '`':
            newList[i-positions] = myList[i]
        else: positions += 1
    myList[:] = newList[:]

if __name__ == '__main__': 
    myList = [0,8,8,8,6,6,5,1,2]
    removeDuplicates(myList)
    print(myList)

    

from random import randrange
def shuffle(myList):
    taken, newList = myList[:], myList[:]
    length = len(myList)
    for i in range(length):
        taken[i] = ''
    iterations = 0
    for i in range(length):
        correct = False
        while not correct:
            rnum = randrange(0, length)
            if rnum not in taken:
                print(rnum)
                print(taken)
                newList[rnum] = myList[i]
                taken[i] = rnum
                iterations += 1
                correct = True
    return newList

myList = [1,2,3,4]

print(shuffle(myList))
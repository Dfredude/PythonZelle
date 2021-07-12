def count(list, x):
    count = 0
    for i in list: 
        if i == x: count += 1
    return count

def isin(list, x):
    status = False
    for i in list:
        if i == x: status = True
    return status

def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x: return i

def reverse(myList):
    list_length = list(range(len(myList)))
    numbers = list_length[-1]
    for i in range(numbers, 0, -1):
        list_length[-i-1] = myList[i]
        print(list_length, myList[i])
    list_length[-1] = myList[0]
    return list_length

def sort(myList):
    newList = []
    for num in myList:
        for i in range(len(newList)):
            if num >= newList[i]:
                newList[i+1] = num
        else: newList[:] = num

def main():
    myList = [5,8,8,3,1]
    print(count(myList, 8), isin(myList, 1), index(myList,8), reverse(myList))

main()

    
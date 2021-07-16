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
    sorted = False      
    while not sorted:
        sorted = True
        for i in range(1, len(myList)):
            if myList[i-1] > myList[i]:
                myList[i-1], myList[i] = myList[i], myList[i-1]
                sorted = False

def main():
    myList = [5,8,8,3,1]
    print(count(myList, 8), isin(myList, 1), index(myList,8), reverse(myList))
    sort(myList)
    print(myList)

main()

    
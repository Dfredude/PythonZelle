import time as t
from random import randint
def main():
    #Testing the algorithms
    n = int(input("Enter the length of a list to use for testing selection and merge sorting algorithms: "))
    myList = [randint(0,100) for i in range(n)]
    print("Random list to sort: ", myList)
    s_time = t.time()
    sortedListByMerge = mergeSort(myList)
    finish_time = t.time()
    merge_total_time = finish_time - s_time
    print("Sorted list by merge: ", sortedListByMerge, sep='\n')
    s_time = t.time()
    selectionSort(myList)
    finish_time = t.time()
    selection_total_time = finish_time - s_time
    print("Sorted list by selection: ", myList, sep= '\n')
    print("Merge sort took: ", merge_total_time)
    print("Selection sort took: ", selection_total_time)


def selectionSort(sequence:list):
    n = len(sequence)
    for bottom in range(n-1):
        ti = bottom
        for i in range(bottom+1, n):
            if sequence[i] < sequence[ti]:
                ti = i
        sequence[bottom], sequence[ti] = sequence[ti], sequence[bottom]

def mergeSort(seq:list):
    n = len(seq)
    if n == 2:
        if seq[0] > seq[1]:
            newList = [seq[1], seq[0]]
        else: newList = seq[:]
    elif n == 1:
        newList = seq[:]
    else:
        newList = []
        list1 = mergeSort(seq[:n//2])
        list2 = mergeSort(seq[n//2:])
        while len(list1) + len(list2) > 0:
            if len(list1) < 1: 
                newList += list2
                list2 = []
            elif len(list2) < 1: 
                newList += list1
                list1 = []
            elif list1[0] < list2[0]:
                item = list1[0]
                newList.append(item)
                list1.remove(item)
            else:
                item = list2[0]
                newList.append(item)
                list2.remove(item)
    return newList


if __name__ == "__main__": main()
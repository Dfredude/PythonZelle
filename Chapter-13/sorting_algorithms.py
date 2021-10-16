import time as t
from random import randint
def main():
    #Testing the algorithms
    myList = [randint(0,1000) for i in range(1000)]
    s_time = t.time()
    selectionSort(myList)
    finish_time = t.time()
    print(myList)
    print("Selection sort took: ", finish_time - s_time)

def selectionSort(sequence:list):
    n = len(sequence)
    for bottom in range(n-1):
        ti = bottom
        for i in range(bottom+1, n):
            if sequence[i] < sequence[ti]:
                ti = i
        sequence[bottom], sequence[ti] = sequence[ti], sequence[bottom]

if __name__ == "__main__": main()
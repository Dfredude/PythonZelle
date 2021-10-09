
def main():
    print(linearSearch(2, [2,3,5,1,2,9]))
    print(binarySearch(2, [1,2,3,5,6,9]))

#This is a linear time/n algorithm. Time required is linearly/proportional to the size 'n' of the sequence;
def linearSearch(item, sequence:list):
    for i in range(len(sequence)):
        if sequence[i] == item:
            return i
    return -1

#This is a log time algorithm, each iteration doubles the problem/sequence size
def binarySearch(item, sorted_sequence:list):
    high = len(sorted_sequence) - 1
    low = 0
    mid = high//2
    while low <= high:
        if item > sorted_sequence[mid]: 
            low = mid
            mid = (mid+high)//2
        elif item < sorted_sequence[mid]:
            high = mid
            mid = mid//2
        elif item == sorted_sequence[mid]: return mid


if __name__ == "__main__":
    main()
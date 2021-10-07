
def main():
    print(linearSearch(2, [2,3,5,1,2,9]))

def linearSearch(item, sequence:list):
    for i in range(len(sequence)):
        if sequence[i] == item:
            return i
    return -1

if __name__ == "__main__":
    main()
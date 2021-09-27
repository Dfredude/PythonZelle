

def max(list_of_numbers:list):
    if len(list_of_numbers) <= 1:
        return list_of_numbers[0]
    elif list_of_numbers[1] > list_of_numbers[0]:
        return max(list_of_numbers[1:])
    else:
        rec_list = list_of_numbers[2:]
        rec_list.append(list_of_numbers[0])
        return max(rec_list)

def main():
    maxNum = max([1,0,4, 2, 8, 3])
    print(maxNum)

if __name__ == "__main__":
    main()
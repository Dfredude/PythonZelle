def squareEach(numbers):
    sq_numbers = []
    for i in range(len(numbers)):
        sq_numbers.append(numbers[i] ** 2)
    return sq_numbers

def sumList(numbers):
    j = 0
    for i in numbers: j+= i
    return j

def modifyListToNumbers(str_list):
    intlist = []
    for i in range(len(str_list)):
        intlist.append(int(str_list[i]))
    return intlist    

def main():
    infile = open('test_scores.txt', 'r')
    str_list = infile.readlines()
    intlist = modifyListToNumbers(str_list[0:-1])
    result = squareEach(intlist)
    infile.close()
    outfile = open('new test scores.txt', 'w')
    print(result, file = outfile) 

main()
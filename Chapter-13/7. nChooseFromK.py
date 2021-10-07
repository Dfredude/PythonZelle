import time

def main():
    print("""This program is simply testing two ways of getting the number of posibilities of
combinations K among N""")
    number_of_elements, amount_to_be_selected = str(input("Enter 2 numbers, separated by a comma (n,k) 'n' should be bigger than 'k': ")).split(',')
    time
    number_of_elements, amount_to_be_selected = int(number_of_elements), int(amount_to_be_selected)
    V1StartTime = time.time()
    V1 = nChooseKVI(number_of_elements, amount_to_be_selected)
    TV1 = time.time() - V1StartTime
    V2StartTime = time.time()
    V2 = nChooseKV2(number_of_elements, amount_to_be_selected)
    TV2 = time.time() - V2StartTime
    printOutput(V1, V2, TV1, TV2)

def printOutput(v1_result, v2_result, v1_time, v2_time):
    print("  V1 result is: ", v1_result, " and V2 is: ", v2_result)
    print("""  Time they took doing the operation  
    V1            v2""")
    print("  {0:9^.4f}\t{1:9^.4f}".format(v1_time, v2_time))

def nChooseKVI(n, k):
    return loopingFactorial(n) // (loopingFactorial(k) * loopingFactorial(n-k))

def loopingFactorial(number):
    for i in range(number-1, 0, -1):
        number = number*i
    return number

def nChooseKV2(n, k):
    if n < k: return 0
    elif k == 1: return n
    else: 
        return nChooseKV2(n-1, k-1) + nChooseKV2(n-1, k)

if __name__ == "__main__": main()

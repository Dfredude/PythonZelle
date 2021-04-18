def squareEach(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
    return

def main():
    numbers = [5,9,8,6,3]
    print(squareEach(numbers))
    print(numbers)

main()
n = int(input("How many numbers would you like to sum up: "))
numbers = []
for i in range(n):
    if i == 0:
        numbers.append(float(input('Enter the 1st number: ')))
    else:
        numbers.append(float(input('Enter the next number: ')))

print(sum(numbers))
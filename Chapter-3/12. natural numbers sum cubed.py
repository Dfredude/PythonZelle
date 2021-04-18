n = int(input("Enter a natural number: "))
numbers = []
for i in range(1,n+1):
    numbers.append(i**3)
print(sum(numbers))
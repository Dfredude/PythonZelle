import math
n = (int(input("How many time would you like to sum up the series: ")))*3
numbers = []
for i in range(1, (n+1), 4):
    numbers.append(4/i)
for i in range(3, (n+1), 4):
    numbers.append(-4/i)
difference = math.pi-(sum(numbers))
print(sum(numbers))
print(difference)
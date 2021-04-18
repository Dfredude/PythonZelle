import math
def fibonacci(iteration):
    print(1)
    n = 0
    for i in range(iteration):
        if n == 0:
            n = 1
            m = 0
            print(n)
            i += 1
        if n >= 1:
            l = n
            n += m
            m = l
            print(n)
            i += 1

fibonacci(5)

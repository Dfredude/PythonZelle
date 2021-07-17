from math import isqrt

def Eratosthenes(n):
    if n <= 2: return []
    numbers = [i for i in range(2,n+1)]
    for i in range(n-2):
        if numbers[i] != 0:
            for j in range(i+1, n-2):
                if numbers[j]%numbers[i] == 0:
                    numbers[j] = 0
    return [numbers[i] for i in range(len(numbers)) if numbers[i] != 0]

if __name__ == '__main__': print(Eratosthenes(120))

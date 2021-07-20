from math import sqrt
from random import randrange

class StatSet:
    def __init__(self) -> None:
        self.values = []

    def addNumber(self, x): self.values.append(x)

    def mean(self): return sum(self.values)/len(self.values)

    def median(self): 
        self.n = len(self.values)
        if self.n % 2 != 0: self.median = self.values[self.n//2+1]
        else: 
            m = self.n/2
            self.median = (self.values[m] + self.values[m+1]) / 2
        return self.median

    def stdDev(self):
        sumDevSq = 0
        xbar = self.mean()
        for num in self.values:
            dev = num - xbar
            sumDevSq = sumDevSq + dev * dev
        return sqrt(sumDevSq/(len(self.values)-1))

    def count(self): return len(self.values)

    def min(self): return min(self.values)

    def max(self): return max(self.values)

def main():
    mySet = StatSet()
    for i in range(10):
        mySet.addNumber(randrange(1,10))
    print(mySet.mean(), mySet.stdDev())

if __name__ == '__main__': main()

    
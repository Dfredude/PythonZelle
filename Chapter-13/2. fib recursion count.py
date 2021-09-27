recursion = 0

def main():
    fibonnaci = fib()
    print("Answer = ", fibonnaci.calcFib(21), "\nRecursions needed = ", fibonnaci.recursion)

class fib:
    def __init__(self) -> None:
        self.recursion = 0
    
    def calcFib(self, n):
        if n < 3:
            return 1
        else:
            self.recursion += 1
            return self.calcFib(n-1) + self.calcFib(n-2)

if __name__ == "__main__":
    main()

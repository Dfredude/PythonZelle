
def main():
    print(fib(11))

def fib(n):
    if n < 3:
        print("Base case: computing {0}".format(n))
        return 1
    else:
        print("Recursion: computing {0}".format(n))
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    main()

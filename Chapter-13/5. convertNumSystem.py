#Using recursion

def baseConversion(num, base):
    if num > base:
        result = baseConversion(num//base, base)
        result.append(num%base)
        return result
    else:
        return [num]

def main():
    print(baseConversion(65161, 16))

if __name__ == "__main__":
    main()
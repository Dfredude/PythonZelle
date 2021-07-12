from math import sqrt

def getNumbers():
    nums= []
    xStr = input('Enter a number(<Enter> to quit) >> ')
    while xStr != '':
        x = float(xStr)
        nums.append(x)
        xStr = input('Enter a number(<Enter> to quit) >> ')
    return nums

def mean(nums):
    total = 0
    for num in nums:
        total = total + num
    return total / len(nums)

def stdDev(nums):
    sumDevSq = 0
    xbar = mean(nums)
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))
def meanStdDev(nums):
    return mean(nums), stdDev(nums)

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0: med = (nums[midPos] + nums[midPos-1]) / 2
    else: med = nums[midPos]
    return med

def main():
    print('This program computes mean, median, and standard deviation.')

    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)
    print('\nThe mean is', xbar)
    print('The standard deviation is', std)
    print('The median is', med)

if __name__ == '__main__': main()
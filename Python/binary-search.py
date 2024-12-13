from util import time_it


@time_it
def leanerSearch(arr, num):
    for index, val in enumerate(arr):
        if val == num:
            return index
    return -1


@time_it
def binarySearch(arr, num):
    leftIndex = 0
    rightIndex = len(arr) - 1
    midIndex = 0
    while leftIndex <= rightIndex:
        midIndex = (leftIndex + rightIndex) // 2
        minNum = arr[midIndex]
        if num == minNum:
            return midIndex
        if num > minNum:
            leftIndex = midIndex + 1
        else:
            rightIndex = midIndex - 1

    return -1


# @time_it
def binarySearchRecursive(arr, num, leftIndex, rightIndex):
    if rightIndex < leftIndex:
        return -1
    midIndex = (leftIndex + rightIndex) // 2
    if midIndex >= len(arr) or midIndex<0:
        return -1
    minNum = arr[midIndex]
    if num == minNum:
        return midIndex
    if num > minNum:
        leftIndex = midIndex + 1
    else:
        rightIndex = midIndex - 1
    return binarySearchRecursive(arr, num, leftIndex, rightIndex)


if __name__ == "__main__":

    arr = [i for i in range(1000000)]
    val = 999999
    arr.sort()

    print(binarySearchRecursive(arr, val, 0, (len(arr) - 1)))
    # print(leanerSearch(arr, val))
    print(binarySearch(arr, val))

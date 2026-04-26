import random
import time


def bubbleSort(nums):
    numLength = len(nums) - 1

    for i in range(numLength):
        for j in range(numLength - i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


def selectionSort(nums):
    numLength = len(nums) - 1

    for i in range(numLength):
        minPlace = i

        for j in range(i + 1, numLength + 1):
            if nums[j] < nums[minPlace]:
                minPlace = j

        temp = nums[i]
        nums[i] = nums[minPlace]
        nums[minPlace] = temp


def insertionSort(nums):
    numLength = len(nums)

    for i in range(1, numLength):
        temp = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = temp


def merge(nums, firstPos, midPos, lastPos):
    leftHalf = []
    rightHalf = []

    for i in range(firstPos, midPos + 1):
        leftHalf.append(nums[i])

    for i in range(midPos + 1, lastPos + 1):
        rightHalf.append(nums[i])

    leftLength = len(leftHalf)
    rightLength = len(rightHalf)

    leftPos = 0
    rightPos = 0
    currentPos = firstPos

    while leftPos < leftLength and rightPos < rightLength:
        if leftHalf[leftPos] <= rightHalf[rightPos]:
            nums[currentPos] = leftHalf[leftPos]
            leftPos += 1
        else:
            nums[currentPos] = rightHalf[rightPos]
            rightPos += 1

        currentPos += 1

    for i in range(leftPos, leftLength):
        nums[currentPos] = leftHalf[i]
        currentPos += 1

    for i in range(rightPos, rightLength):
        nums[currentPos] = rightHalf[i]
        currentPos += 1

    #def mergesort(nums):
    #     n = len(nums)
    # size = 1
    # while size < n:
    #     left = 0
    #     while left < n - 1:
    #         mid = min(left + size - 1, n - 1)
    #         right = min(left + (2 * size) - 1, n - 1)
    #         merge(nums, left, mid, right)
    #         left += 2 * size
    #     size *= 2

def mergeSort(nums, firstPos, lastPos):
    if firstPos < lastPos:
        midPos = (firstPos + lastPos) // 2

        mergeSort(nums, firstPos, midPos)

        mergeSort(nums, midPos + 1, lastPos)

        merge(nums, firstPos, midPos, lastPos)


def rearange(nums, firstPos, lastPos):
    comp = nums[lastPos]

    smallerEnd = firstPos - 1

    for currentPos in range(firstPos, lastPos):
        if nums[currentPos] < comp:
            smallerEnd += 1

            temp = nums[smallerEnd]
            nums[smallerEnd] = nums[currentPos]
            nums[currentPos] = temp

    temp = nums[smallerEnd + 1]
    nums[smallerEnd + 1] = nums[lastPos]
    nums[lastPos] = temp

    return smallerEnd + 1


def quickSort(nums, firstPos, lastPos):
    if firstPos < lastPos:
        splitPos = rearange(nums, firstPos, lastPos)

        quickSort(nums, firstPos, splitPos - 1)

        quickSort(nums, splitPos + 1, lastPos)


def main():
    nums = []
    numAmount = 10000

    for i in range(numAmount):
        nums.append(random.randint(1, 100000))

    print("We are Sorting", numAmount, "numbers just for you :D")
    print( )


    bubbleNums = nums.copy()
    builtInNums = nums.copy()
    quickNums = nums.copy()
    insertionNums = nums.copy()
    mergeNums = nums.copy()
    selectionNums = nums.copy()

    mergeLength = (len(mergeNums) - 1)
    quickLength = (len(quickNums) - 1)

    startTime = time.time()
    bubbleSort(bubbleNums)
    endTime = time.time()
    print("Bubble Sort has completed after ", (endTime - startTime) * 1000, "ms")
    startTime = endTime
    selectionSort(selectionNums)
    endTime = time.time()
    print("Selection Sort has completed after ", (endTime - startTime) * 1000, "ms")
    startTime = endTime
    insertionSort(insertionNums)
    endTime = time.time()
    print("Insrtion Sort has completed after ", (endTime - startTime) * 1000, "ms")
    startTime = endTime
    mergeSort(mergeNums, 0, mergeLength)
    endTime = time.time()
    print("Merge Sort has completed after ", (endTime - startTime) * 1000, "ms")
    startTime = endTime
    quickSort(quickNums, 0, quickLength)
    endTime = time.time()
    print("Quick Sort has completed after ", (endTime - startTime) * 1000, "ms")
    startTime = endTime
    builtInNums.sort()
    endTime = time.time()
    print("Built in sort has completed after ", (endTime - startTime) * 1000, "ms")


main()
import os
import heapq


class Node:
    def __init__(self, char, frequency):

        self.char = char
        self.frequency = frequency
        self.leftChild = None
        self.rightChild = None

    # i had alot of trouble with 
    # this section, and ended up
    # implementing it from a video
    # https://www.youtube.com/watch?v=JCOph23TQTY
    # it is overloading the less than and equals operators
    # for later use in my code. 

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, Node) ):
            return False
        return self.frequency == other.frequency

    # end of section implemented from the video


def makeTree(frequency):
    queue = []

    for char in frequency:
        freq = frequency[char]
        node = Node(char, freq)
        heapItem = (freq, node)
        heapq.heappush(queue, heapItem)

    queueSize = len(queue)

    while queueSize > 1:

        leftItem = heapq.heappop(queue)
        leftFreq = leftItem[0]
        leftNode = leftItem[1]
        rightItem = heapq.heappop(queue)
        rightFreq = rightItem[0]
        rightNode = rightItem[1]
        parentFreq = leftFreq + rightFreq
        parent = Node(None, parentFreq)
        parent.leftChild = leftNode
        parent.rightChild = rightNode
        heapItem = (parentFreq, parent)
        heapq.heappush(queue, heapItem)

        queueSize = len(queue)

    final = heapq.heappop(queue)
    root = final[1]

    return root


def makeCode(node, currentCode, codes):
    if node is None:
        return

    if node.char is not None:
        if currentCode == "":
            currentCode = "0"

        codes[node.char] = currentCode
        return

    makeCode(node.leftChild, currentCode + "0", codes)
    makeCode(node.rightChild, currentCode + "1", codes)


def makeEstring(originalString, codes):
    encodedString = ""

    for char in originalString:
        encodedString += codes[char]

    return encodedString


def getOriginal(encodedString, root):
    originalString = ""
    current = root

    for bit in encodedString:
        if bit == "0":
            current = current.leftChild
        else:
            current = current.rightChild

        if current.char is not None:
            originalString += current.char
            current = root

    return originalString


def main():
    print("Huffman Coding ")
    print("1. Input Text")
    print("2. Load a file")

    choice = input("Choice: ")

    originalString = ""

    if choice == "1":
        originalString = input("Enter text :")

    else:
        filename = input("Enter file name: ")
        file = open(filename, "r")
        originalString = file.read()
        file.close()

    frequency = {}

    for char in originalString:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    root = makeTree(frequency)

    codes = {}
    makeCode(root, "", codes)

    encodedString = makeEstring(originalString, codes)
    original = getOriginal(encodedString, root)

    print("\n")
    print("Input Text:")
    print(originalString)

    print("\n")
    print("Huffman Codes:")
    for char in codes:
        if char == " ":
            print(" :", codes[char])
        else:
            print(char + ":", codes[char])

    print("\n")
    print("Encoded string:")
    print(encodedString)

    print("\n")
    print("Original string:")
    print(original)

    originalSize = len(originalString) * 8
    compressedSize = len(encodedString)

    print("\n")
    print("Compression Statistics:")
    print("Original size:", originalSize, "bits")
    print("Compresed size:", compressedSize, "bits")

    if compressedSize > 0:
        cSize = round(originalSize / compressedSize, 2)
        print("Compression ratio:", cSize)

    print("\n")

    if originalString == original:
        print("\n")
        print("Everything went according to plan, ")
        print("Expected ", original, "got ", originalString)
    else:
        print("\n")
        print("Everything did not go acording to plan")
        print("Expected ", original, "got ", originalString)

main()
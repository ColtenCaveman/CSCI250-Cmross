class Heap:
    def __init__(self):
        self.elements = []
        self.sizeOfHeap = 0

    def size(self):

        heapSize = self.sizeOfHeap
        return heapSize

    def is_empty(self):
        if self.sizeOfHeap == 0:
            
            return True
        else:

            return False

    def __str__(self):

        heap = str(self.elements)

        return heap

    def insert(self, key):

        self.elements.append(key)
        tempsize = self.sizeOfHeap 
        self.sizeOfHeap = self.sizeOfHeap + 1
        self.heapify_up(tempsize)

    def heapify_up(self, index):

        done = False

        while done == False:

            if index == 0:
                done = True

            else:
                parent = (index - 1) // 2
                if self.elements[index] >= self.elements[parent]:
                    done = True

                else:
                    temp = self.elements[index]
                    self.elements[index] = self.elements[parent]
                    self.elements[parent] = temp
                    index = parent

    def peek(self):

        if self.is_empty():
            return
        smallest = self.elements[0]

        return smallest
    
    def extract_min(self):

        if self.sizeOfHeap == 0:
            return

        littleOne = self.elements[0]
        last = self.elements[self.sizeOfHeap - 1]
        self.elements[0] = last
        self.elements.pop()
        self.sizeOfHeap = self.sizeOfHeap - 1

        if self.sizeOfHeap > 0:
            self.heapify_down(0)

        return littleOne

    def heapify_down(self, index):

        done = False

        while done == False:

            firstChild = (index * 2) + 1
            secondChild = (index * 2) + 2
            smallest = index

            if firstChild <= self.sizeOfHeap - 1:
                if self.elements[firstChild] < self.elements[smallest]:
                    smallest = firstChild

            if secondChild <= self.sizeOfHeap - 1:
                if self.elements[secondChild] < self.elements[smallest]:
                    smallest = secondChild

            if smallest == index:
                done = True

            else:
                temp = self.elements[index]
                self.elements[index] = self.elements[smallest]
                self.elements[smallest] = temp
                index = smallest

    def build_heap(self, array):

        self.elements = array.copy()
        self.sizeOfHeap = len(array)

        beginning = (self.sizeOfHeap // 2) - 1

        for index in range(beginning, -1, -1):
            self.heapify_down(index)

    def decrease_key(self, index, new_key):

        currentValue = self.elements[index]

        if new_key > currentValue:
            raise Exception("Exception has been raised, new key is greater than curent key")

        else:
            self.elements[index] = new_key
            self.heapify_up(index)

    def delete(self, index):

        smallest = float("-inf")
        self.decrease_key(index, smallest)
        self.extract_min()
        
def heap_sort(array):

    heap = Heap()
    heap.build_heap(array)
    sortedList = []
    amount = heap.size()

    for index in range(amount):

        smallestValue = heap.extract_min()
        sortedList.append(smallestValue)

    return sortedList

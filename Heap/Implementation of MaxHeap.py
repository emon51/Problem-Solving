
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0 
    
    def append(self, newval: int) -> None:
        self.heap.append(newval)
        self.size += 1

        self.shiftUp(self.size - 1)


    def pop(self) -> int: #Popped max value and return.
        maxitem = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        
        self.shiftDown(0)
        return maxitem


    def shiftUp(self, i):
        while 0 < i and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
        

    def shiftDown(self, i):
        largest = i 
        if self.left(i) < self.size and self.heap[largest] < self.heap[self.left(i)]:
            largest = self.left(i)
        if self.right(i) < self.size and self.heap[largest] < self.heap[self.right(i)]:
            largest = self.right(i)
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.shiftDown(largest)


    def parent(self, i):
        return i // 2 
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
#==========================================================================================================#

if __name__ == '__main__':

    maxheap = MaxHeap()
    maxheap.append(5)
    maxheap.append(3)
    maxheap.append(10)
    maxheap.append(8)
    maxheap.append(70)
    #print(maxheap.heap)
    #print(maxheap.size)
    #print(maxheap.pop())
    #print(maxheap.heap)

    res = []
    while maxheap.size > 0:
        val = maxheap.pop()
        res.append(val)
    
    #print(res)

    #Convert list to heap 
    arr = [7, 3, 1, 9, 2, 6, 4, 7, 5, 8]

    hp = MaxHeap()
    for num in arr:
        hp.append(num)
    print(hp.heap)

    res = []
    while hp.size > 0:
        val = hp.pop()
        res.append(val)
    print(res)
    



    

class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        if self.rightMinHeap and num > self.rightMinHeap[0]:
            heapq.heappush(self.rightMinHeap, num)
        else:
            heapq.heappush(self.leftMaxHeap, -num)

        if (len(self.leftMaxHeap) - len(self.rightMinHeap)) > 1:
            heapq.heappush(self.rightMinHeap, -heapq.heappop(self.leftMaxHeap))
        elif (len(self.rightMinHeap) - len(self.leftMaxHeap)) > 1:
            heapq.heappush(self.leftMaxHeap, -heapq.heappop(self.rightMinHeap))

    def findMedian(self) -> float:
        if (len(self.leftMaxHeap) + len(self.rightMinHeap)) % 2 == 0:
            return (-self.leftMaxHeap[0] + self.rightMinHeap[0]) / 2
    
        if len(self.leftMaxHeap) > len(self.rightMinHeap):
            return -self.leftMaxHeap[0]
        else:
            return self.rightMinHeap[0]
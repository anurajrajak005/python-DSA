# code first in MedianFinder

class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()


    def findMedian(self) -> float:
        mid = len(self.stream) // 2
        if len(self.stream) % 2 == 0:
            return (self.stream[mid] + self.stream[mid - 1]) / 2

        else:
            return self.stream[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
 

# code Second in MedianFinder using heap short 

from heapq import heapify, heappop, heappush
class MedianFinder:
    def __init__(self):
        self.left, self.right = [], []
    def addNum(self, num: int) -> None:
        heappush(self.left, -num)
        heappush(self.right, -heappop(self.left))
        if len(self.right)>len(self.left):
            heappush(self.left, -heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left)==len(self.right):
            return ((-self.left[0])+self.right[0])/2
        return -self.left[0]            







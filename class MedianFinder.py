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
 
import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        largest_small = -heapq.heappop(self.small)
        heapq.heappush(self.large, largest_small)

        if len(self.small) < len(self.large):
            smallest_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_large)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
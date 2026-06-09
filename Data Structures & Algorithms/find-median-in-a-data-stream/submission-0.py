class MedianFinder:

    def __init__(self):
        # 用兩個heap 來維持中位數
        self.count = 0
        self.smaller_heap = [] # 小的這部分要取負數 
        self.bigger_heap = []

    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.smaller_heap, -num)
        val = heapq.heappop(self.smaller_heap)
        heapq.heappush(self.bigger_heap, -val)

        if self.count % 2 == 1:
            val = heapq.heappop(self.bigger_heap)
            heapq.heappush(self.smaller_heap, -val)

    def findMedian(self) -> float:
        if self.count % 2 == 1:
            return float(-self.smaller_heap[0])
        else:
            return (-self.smaller_heap[0] + self.bigger_heap[0]) / 2.0
        
        
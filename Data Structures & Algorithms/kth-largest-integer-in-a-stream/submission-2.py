class KthLargest:
    # heap / priority queue
    # 找到k個 最大元素 可以包含一樣的數
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        # 1. 將傳入的 list 直接原地轉換成堆積 (Heapify)，時間複雜度為 O(N)
        heapq.heapify(self.heap)    
        # 2. 如果堆積裡的元素超過 k 個，就把最小的彈出，直到剩下 k 個
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 3. 把新元素推進堆積中
        heapq.heappush(self.heap, val)
        # 4. 如果堆積長度超過 k，把最小的（頂端）彈出
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # 5. 此時堆積頂端 (index 0) 就是目前第 k 大的元素
        return self.heap[0]

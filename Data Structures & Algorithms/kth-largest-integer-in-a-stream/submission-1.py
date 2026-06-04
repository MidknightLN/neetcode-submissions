class KthLargest:
    # heap / priority queue
    # 找到k個 最大元素 可以包含一樣的數
    def __init__(self, k: int, nums: List[int]):
        self.q = sorted(nums, reverse=True)[:k]
        self.k = k
        

    def add(self, val: int) -> int:
        self.q.append(val)
        self.q = sorted(self.q, reverse=True)[:self.k]
        return self.q[-1]
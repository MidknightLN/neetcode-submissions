class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        # 排序KEY 但是用 value排   count.get 等價於 count[x] 
        # 只是因為這裡的x 無法表明 如果硬要用需要使用 lambda
        return sorted(count.keys(), key=count.get)[-k:]
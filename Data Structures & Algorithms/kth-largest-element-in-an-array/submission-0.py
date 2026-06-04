class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 要找第Ｋ個大的元素 >> 小的彈出

        import heapq
        hq = nums[:k]
        heapq.heapify(hq)

        for idx in range(k, len(nums)):
            if nums[idx] > hq[0]:
                heapq.heappush(hq, nums[idx])
                heapq.heappop(hq)

        return hq[0]
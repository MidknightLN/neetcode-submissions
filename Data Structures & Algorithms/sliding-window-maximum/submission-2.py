class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        visit = [0 for _ in range(len(nums)-k+1)]

        l = 0
        while l + k - 1 < len(nums):
            visit[l] = max(nums[l:l+k])
            l += 1
        return visit
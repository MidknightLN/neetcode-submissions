class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-float('inf') for _ in range(len(nums))]
        dp[0] = max(dp[0], nums[0])

        for idx in range(1, len(nums)):
            dp[idx] = max(nums[idx], dp[idx-1]+nums[idx])
        
        return max(dp)
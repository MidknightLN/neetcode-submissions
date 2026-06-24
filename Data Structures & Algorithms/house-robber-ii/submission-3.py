class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])


        def liner(line:list[int]) -> int:
            dp = [0 for _ in range(len(line))]
            dp[0] = line[0]
            dp[1] = max(line[0], line[1])

            for i in range(2, len(line)):
                dp[i] = max(dp[i-2] + line[i], dp[i-1])
            return dp[-1]

        res1 = liner(nums[:-1])
        res2 = liner(nums[1:])

        return max(res1, res2)
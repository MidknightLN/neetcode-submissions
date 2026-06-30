class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax = 1
        currMin = 1

        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
                continue
            tempMax = currMax*n
            tempMin = currMin*n
            currMax = max(tempMax, tempMin, n)
            currMin = min(tempMax, tempMin, n)
            res = max(res, currMax)
        return res
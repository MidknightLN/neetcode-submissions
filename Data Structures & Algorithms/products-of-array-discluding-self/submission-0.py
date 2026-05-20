class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        L = len(nums)
        res = [1 for _ in range(L)]

        temp = 1
        for idx in range(L):
            res[idx] *= temp
            temp *= nums[idx]
        
        temp = 1
        for idx in range(L-1, -1, -1):
            res[idx] *= temp
            temp *= nums[idx]
        

        return res

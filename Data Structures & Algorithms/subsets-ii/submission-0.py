class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []

        def backtracking(count):
            if count >= len(nums):
                res.append(subset[:])
                return
            # remove repeat

            # 1 choose
            subset.append(nums[count])
            backtracking(count+1)
            # 2 not choose
            subset.pop()
            # Move the pointer until we find a new number
            while count + 1 < len(nums) and nums[count] == nums[count + 1]:
                count += 1
            backtracking(count+1)
        
        backtracking(0)
        return res


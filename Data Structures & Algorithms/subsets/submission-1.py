class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## dfs
        res = []

        subset = []
        def dfs(idx:int):
            if idx >= len(nums):
                res.append(subset[:])
                return
            # 決定新增當前元素
            subset.append(nums[idx])
            dfs(idx+1)
            # 決定“不要”新增當前元素
            subset.pop()
            dfs(idx+1)
        
        dfs(0)
        return res
            
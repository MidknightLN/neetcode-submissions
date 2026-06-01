class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []
        def backtracking(pointer, remain):
            # 剛好符合就加入
            if remain == 0:
                res.append(subset[:])
                return 
            # 超出規則無效就不理
            if remain < 0 or pointer < 0:
                return 
            
            # 選擇1 加入當前元素
            if nums[pointer] <= remain:
                subset.append(nums[pointer])
                backtracking(pointer, remain-nums[pointer])
                subset.pop()
            # 選擇2 不加入當前元素
            backtracking(pointer-1, remain)

        # Main
        pointer = len(nums) -1
        backtracking(pointer, target)
        return res
            
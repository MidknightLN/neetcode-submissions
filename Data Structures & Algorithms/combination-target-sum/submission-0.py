class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        pointer = len(nums) -1
        def backtracking(pointer, remain):
            if remain == 0:
                res.append(subset[:])
                return 

            # 用迴圈嘗試加入 >> 選擇2本身就包含在這個for 迴圈中
            for i in range(pointer, -1, -1):
                if nums[i] > remain:
                    continue
                # 選擇1 加入目前可以加入的最大元素
                subset.append(nums[i])
                backtracking(i, remain-nums[i])
                # 回朔狀態
                subset.pop()

        backtracking(pointer, target)
        return res

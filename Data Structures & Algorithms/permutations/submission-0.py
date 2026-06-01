class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        visited = [0 for _ in range(len(nums))]
        def backtracking(index):
            # 長度相等就代表填完了
            if index >= len(nums):
                res.append(subset[:])
                return 

            for i in range(len(nums)):
                # 如果這格已經用過了就跳過
                if visited[i] == 1:
                    continue
                
                # 選擇使用這格
                subset.append(nums[i])
                visited[i] = True
                backtracking(index+1)
                # 回朔
                subset.pop()
                visited[i] = False
        
        backtracking(0)
        return res




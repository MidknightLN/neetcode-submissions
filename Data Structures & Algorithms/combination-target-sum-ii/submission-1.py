class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []

        def backtracking(index, remain):
            # 符合答案
            if remain == 0:
                res.append(subset[:])
                return 
            # 超出限制
            if index >= len(candidates) or candidates[index] > remain:
                return
            
            # 開始構造
            for i in range(index, len(candidates)):
                # 【修改點 1】優化剪枝：如果當前數字已經大於 remain，後面的更大，直接 break 結束這個迴圈
                if candidates[i] > remain:
                    break
                # 如果跟前一個元素相同，代表前面已經做過一模一樣的事情了，直接跳過
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                    
                subset.append(candidates[i])
                backtracking(i+1, remain-candidates[i])
                subset.pop()

        backtracking(0, target)
        return res
        



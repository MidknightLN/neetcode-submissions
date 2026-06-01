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
            # 剪枝：因為從小到大，如果當前數字已經大於剩下的 remain，後面更大的數字更不可能，直接結束
            if index >= len(candidates) or candidates[index] > remain:
                return
                
            # 選擇1 加入
            subset.append(candidates[index])
            backtracking(index+1, remain - candidates[index])
            # 選擇2 不加入
            # 【核心去重】如果要跳過這個數字，後面所有跟它「長得一樣」的數字在這一層都要一起跳過！
            # 否則就會發生「後面重複的數字遞迴進去，選了跟現在一模一樣的值」的情況
            subset.pop()
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            backtracking(next_index, remain)

        backtracking(0, target)
        return res

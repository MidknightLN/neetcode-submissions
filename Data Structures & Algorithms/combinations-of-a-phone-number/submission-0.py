class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []

        subset = []
        letter_map = {
            '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']
        }

        def backtracking(index): 
            # 如果已經滿足長度就回傳
            if index == len(digits):
                res.append(''.join(subset[:]))
                return 
            
            # 其他終止條件？

            # 開始track
            for i in range(len(letter_map[digits[index]])):
                subset.append(letter_map[digits[index]][i])
                backtracking(index+1)
                subset.pop()
        backtracking(0)
        return res
        


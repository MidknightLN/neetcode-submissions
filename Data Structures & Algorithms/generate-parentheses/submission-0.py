class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        subset = []
        def backtracking(left, right):
            # 如果都填寫完畢 代表左右都不剩下
            if left == right == 0:
                res.append("".join(subset))
                return 
            
            if left > 0:
                subset.append('(')
                backtracking(left -1, right)
                subset.pop()
            if left < right: ## 左括號剩下可以放得比右括號 少 代表已經填進去
                subset.append(')')
                backtracking(left, right-1)
                subset.pop()

        backtracking(n, n)
        return res


            

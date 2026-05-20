class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        from collections import Counter
        cols_count = defaultdict(set)
        rows_count = defaultdict(set)
        squares_count = defaultdict(set)

        for idx in range(81):
            r = idx // 9
            c = idx % 9
    
            val = board[r][c]
            if val == '.':
                continue
            sr = r // 3
            sc = c // 3
            ## 用 (sr, sc) 作為Key
            if (val in rows_count[r] or val in cols_count[c] or val in squares_count[(sr, sc)]):
                return False
            rows_count[r].add(val)
            cols_count[c].add(val)
            squares_count[(sr, sc)].add(val)
        return True
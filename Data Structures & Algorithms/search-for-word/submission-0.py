class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        subset = []
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def backtracking(idx, jdx, index:int):
            # 如果找到答案
            if index == len(word):
                return True
            # 如果超出限制 就離開 
            if index > len(word):
                return False
            # 1. 超出邊界
            if not (0 <= idx < len(board) and 0 <= jdx < len(board[0])):
                return False
            # 2. 字元不匹配
            if board[idx][jdx] != word[index]:
                return False

            # 開始找
            temp = board[idx][jdx]
            board[idx][jdx] = '#'
            for dr, dc in direction:
                if backtracking(idx+dr, jdx+dc, index+1):
                    return True
            board[idx][jdx] = temp
                    
        # 這個是position, word 的index
        for idx in range(len(board)):
                for jdx in range(len(board[0])):
                    if backtracking(idx, jdx, 0):
                        return True
        return False



            
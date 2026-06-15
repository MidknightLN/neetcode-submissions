class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 逆向做法 從邊緣開始找
        # 全部看完之後 如果還有沒標記過的 'O' 就代表他是被包住的 需要修改
        if not board or not board[0]:
            return 
        
        rows = len(board)
        cols = len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if r<0 or r >= rows or c<0 or c>=cols:
                return 
            if board[r][c] == 'X' or board[r][c] == '#':
                return 
            
            board[r][c] = '#'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return

        for r in range(rows):
            for c in range(cols):
                if r==0 or r==rows-1 or c==0 or c==cols-1:
                    if board[r][c] == 'O':
                        dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
                
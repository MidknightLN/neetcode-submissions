class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 正向檢查
        if not board or not board[0]:
            return 

        rows = len(board)
        cols = len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, curr_island):
            # 如果碰觸到邊緣就回傳 True
            if  r<0 or r>=rows or c<0 or c>=cols:
                return True
            # 如果已經看過或者是Ｘ
            if board[r][c] == 'X' or visited[r][c]:
                return False
            # 紀錄當前是O 而且已經看過
            visited[r][c] = True
            curr_island.append((r, c))
            # 去看上下左右 如果有回傳代表最後碰到邊了
            up = dfs(r-1, c, curr_island)
            down = dfs(r+1, c, curr_island)
            left = dfs(r, c-1, curr_island)
            right = dfs(r, c+1, curr_island)
            return up or down or left or right
        # LOOP
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and not visited[r][c]:
                    island = []
                    if not dfs(r, c, island):
                        for x, y in island:
                            board[x][y] = 'X'
            
        

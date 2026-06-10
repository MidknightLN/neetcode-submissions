class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # 從寶藏開始反向 BFS 嘗試修改 如果更小就修改
        rows, cols = len(grid), len(grid[0])
        q = deque() # 紀錄寶藏位置，之後用來做BFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            cur_x, cur_y = q.popleft()
            for dx, dy in direction:
                nx = cur_x + dx
                ny = cur_y + dy
                if 0<= nx < rows and 0<= ny < cols and grid[nx][ny] == 2147483647:
                    grid[nx][ny] = grid[cur_x][cur_y] +1
                    q.append((nx, ny))



        # 
                
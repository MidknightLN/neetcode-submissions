class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    grid[r][c] = 0
                    q.append((r, c, 0))
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        while q:
            cur_x, cur_y, time= q.popleft()
            for dx, dy in direction:
                nx, ny = cur_x+dx, cur_y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    res = max(res, time+1)
                    q.append((nx, ny, time+1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return res


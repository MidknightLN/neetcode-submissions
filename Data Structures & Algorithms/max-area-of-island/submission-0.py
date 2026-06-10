class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = 0
        rows, cols = len(grid), len(grid[0])
        q = deque()          
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                temp = 0
                if grid[r][c] == 1:
                    temp += 1
                    grid[r][c] = 0
                    q.append((r, c))
                    while q:
                        cr, cc = q.popleft()
                        for dx, dy in direction:
                            nx, ny = cr+dx, cc+dy
                            if  0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1:
                                temp += 1
                                grid[nx][ny] = 0
                                q.append((nx, ny))
                    res = max(res, temp)
        return res

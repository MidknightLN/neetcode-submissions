class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        direction = [(-1,0), (1, 0), (0, -1), (0, 1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # print(r, c)
                    res += 1
                    q.append([r, c])
                    grid[r][c] = '0'
                    while q:
                        r, c = q.popleft()
                        for dx, dy in direction:
                            nx, ny = r + dx, c + dy
                            if 0 <= nx < rows and 0 <= ny < cols:
                                if grid[nx][ny] == '1':
                                    q.append([nx, ny])
                                    grid[nx][ny] = '0'
        return res
                    

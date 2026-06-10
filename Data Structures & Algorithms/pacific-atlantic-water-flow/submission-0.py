class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 檢查每個元素往低處走是否可以抵達 （最左or最上） （最右or最下）
        # 反向檢查 從左邊上面的元素往高處走 and 右邊下面的元素往高處走 兩者取交集
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        LT = [[False] * cols for _ in range(rows)]
        RB = [[False] * cols for _ in range(rows)]
        
        # 先算LT 的 >> 把所有起點放到queue中
        q = deque()
        for c in range(cols):
            LT[0][c] = True
            q.append((0, c))
        for r in range(rows):
            LT[r][0] = True
            q.append((r, 0))
        # 開始擴散
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            cur_x, cur_y = q.popleft()
            for dx, dy in directions:
                nx, ny = cur_x+dx, cur_y+dy
                if 0<=nx<rows and 0<=ny<cols and not LT[nx][ny] and heights[nx][ny] >= heights[cur_x][cur_y]:
                    LT[nx][ny] = True
                    q.append((nx, ny))
                
        # 再來算BR 的
        q = deque()
        for c in range(cols):
            RB[rows-1][c] = True
            q.append((rows-1, c))
        for r in range(rows):
            RB[r][cols-1] = True
            q.append((r, cols-1))
        # 開始擴散
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            cur_x, cur_y = q.popleft()
            for dx, dy in directions:
                nx, ny = cur_x+dx, cur_y+dy
                if 0<=nx<rows and 0<=ny<cols and not RB[nx][ny] and heights[nx][ny] >= heights[cur_x][cur_y]:
                    RB[nx][ny] = True
                    q.append((nx, ny))
        

        # 檢查 交集
        res = []
        for r in range(rows):
            for c in range(cols):
                if LT[r][c] and RB[r][c]:
                    res.append([r, c])
        return res

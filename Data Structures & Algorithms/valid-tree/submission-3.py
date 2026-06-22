class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 把限制轉換成連接圖
        degree = defaultdict(list)

        for p, q in edges:
            degree[q].append(p)
            degree[p].append(q)
        # 這個用來記錄 目前看過哪些
        visited = set()
        # 
        def dfs(node, prev):
            # 如果查到已經看過的node 就代表產生圓環  返回False
            if node in visited:
                return False
            # 沒看過就加入當前node
            visited.add(node)
            # 把它連接的所有node 扣掉來源 繼續找
            for cur in degree[node]:
                if cur == prev:
                    continue
                if not dfs(cur, node):
                    return False
            return True
        # 開始
        if not dfs(0, -1):
            return False
        # 有可能有孤立島嶼 所以最後應該是看 看過的node數量是否相等於目標
        return len(visited) == n
            
        

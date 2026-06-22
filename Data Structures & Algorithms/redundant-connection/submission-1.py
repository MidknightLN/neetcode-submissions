class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 3 <= n <= 100
        parent = list(range(100+1))

        # 找尋根節點
        def find(node):
            if parent[node]  == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        # 比較edge的兩邊根節點是否相同
        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            # 如果edge 兩邊都是相同 根節點 就代表造成迴圈了
            if root_u == root_v:
                return True
            
            # 如果根節點不同，就進行合併：
            # 因為有完全路徑壓縮，這裡直接讓其中一個根節點成為另一個的父親即可
            parent[root_u] = root_v
            return False
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
        

                
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        count = n

        # 找尋根節點
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        # 合併島嶼
        def union(i, j):
            nonlocal count
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if root_i < root_j:
                    parent[root_j] = root_i  # 讓較大的根節點指向較小的
                else:
                    parent[root_i] = root_j
                
                # 成功合併兩座島，總島嶼數量減 1
                count -= 1

        for u, v in edges:
            union(u, v)
        return count

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        count = 0

        def dfs(node):
            for neibor in adj[node]:
                if neibor not in visited:
                    visited.add(neibor)
                    dfs(neibor)
                # 已經看過的不需要理他
                
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
                
        return count
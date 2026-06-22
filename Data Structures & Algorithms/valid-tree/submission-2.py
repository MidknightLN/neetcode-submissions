class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        degree = defaultdict(list)

        for p, q in edges:
            degree[q].append(p)
            degree[p].append(q)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for cur in degree[node]:
                if cur == prev:
                    continue
                if not dfs(cur, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n
            
        

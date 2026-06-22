class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ## DFS

        # 我們一條一條邊加進去。在加入邊 (u, v) 之前，我們先用 DFS 查查：「在目前的圖中，能不能從 u 走到 v？」
        # 如果可以：代表這兩點早就連通了，現在補上這條邊一定會形成環，它就是答案。
        # 如果不行：就把這條邊正式加進鄰接表（Adjacency List）中，繼續看下一條。
        graph = defaultdict(list)

        def has_path(source, target, visited):
            if source == target:
                return True
            visited.add(source)
            for neighbor in graph[source]:
                if neighbor not in visited:
                    if has_path(neighbor, target, visited):
                        return True
            return False

        for u, v in edges:
            # 每次加邊前，先確認 u 是否能走到 v
            if u in graph and v in graph and has_path(u, v, set()):
                return [u, v]
            # 如果走不到，才把邊放進圖裡
            graph[u].append(v)
            graph[v].append(u)
        

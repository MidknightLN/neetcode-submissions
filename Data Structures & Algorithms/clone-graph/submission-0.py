"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        node_map = {node: Node(node.val)} # 從舊的 對應新的
        q = deque([node]) # 裡面放的是舊的node

        while q:
            cur = q.popleft()

            for neibor in cur.neighbors:
                # 如果查不到 舊node 就代表沒建立新node
                if neibor not in node_map:
                    node_map[neibor] = Node(neibor.val)
                    q.append(neibor)
                
                node_map[cur].neighbors.append(node_map[neibor])
        return node_map[node]
                

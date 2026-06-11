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

        node_map = {}

        def dfs(node):
            if node in node_map:
                return node_map[node]

            node_map[node] = Node(node.val)
            if node.neighbors:
                for neibor in node.neighbors:
                    node_map[node].neighbors.append(dfs(neibor))
            return node_map[node]
        
        dfs(node)
        return node_map[node]
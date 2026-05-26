# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        from collections import deque
        q = deque() # node
        node = root
        res = []
        while q or node:
            # DFS
            while node:
                q.append(node)
                node = node.left
            
            # 走到底了
            node = q.pop()
            res.append(node.val)
            # 判斷目前幾個
            if len(res) == k:
                return res[-1]
            # 走右邊
            node = node.right

            
            
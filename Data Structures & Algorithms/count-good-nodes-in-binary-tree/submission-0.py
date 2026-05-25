# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        from collections import deque
        q = deque()
        q.append((root, root.val)) # node, max_val
        
        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                ans += 1
            max_val = max(max_val, node.val)
            if node.left:
                q.append((node.left, max_val))
            if node.right:
                q.append((node.right, max_val))
        return ans
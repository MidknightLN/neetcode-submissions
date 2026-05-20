# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque
        dq = deque()
        dq.append((p, q))

        while dq:
            L, R = dq.popleft()
            if not L and not R:
                continue

            if not L or not R or L.val != R.val:
                return False

            dq.append((L.left, R.left))
            dq.append((L.right, R.right))

        return True

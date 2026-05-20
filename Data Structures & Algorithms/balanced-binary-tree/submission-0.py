# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        res = False

        def dfs(node):
            nonlocal res
            if not node:
                return True, 0 # 左節點高度  右節點高度
            left_state, left_height = dfs(node.left)
            right_state, right_height = dfs(node.right)

            curr_state = left_state and right_state and abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return curr_state, height
        
        s, h = dfs(root)
        return s

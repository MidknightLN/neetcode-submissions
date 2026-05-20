# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node): # return 高度, 最大直徑
            if not node:
                return 0, 0
            
            left_height, left_diam = dfs(node.left)
            right_height, right_diam = dfs(node.right)

            # 計算當前最大高度
            curr_height = 1 + max(left_height, right_height)

            # 計算通過當前節點的直徑 = 左高度＋右高度 # 最大直徑 在三個選擇裡面選
            curr_diam = left_height + right_height
            max_diam = max(curr_diam, left_diam, right_diam)

            return curr_height, max_diam
        
        h, d = dfs(root)
        return d

            

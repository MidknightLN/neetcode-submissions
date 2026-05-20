# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # For any given node, the longest path that passes through it is 
        # the sum of the height of its left subtree and the height of its right subtree.
        # 對於任意兩個節點的最長距離應該等同於 他們共同處節點的 左高度＋右高度
        if not root:
            return 0
        max_depth = 0

        def dfs(node):
            nonlocal max_depth

            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            max_depth = max(max_depth, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return max_depth


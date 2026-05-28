# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #由下而上、挑選單邊、更新全域 (DFS)
        self.max_sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            # 【關鍵剪分支】：如果子樹傳回負數，我們就不要了（取 0）
            left_val = max(dfs(node.left), 0)
            right_val = max(dfs(node.right), 0)

            # 如果以自己當作root 左右最大可以達到的數值，嘗試更新
            current_path = node.val + left_val + right_val  
            self.max_sum = max(self.max_sum, current_path)

            # 如果自己不是root 就要選擇較大的一邊回報
            return node.val + max(left_val, right_val)

        dfs(root)

        return self.max_sum
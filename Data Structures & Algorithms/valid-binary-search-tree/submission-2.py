# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 驗證二分樹
        # 左側都更小
        # 右側都更大
        # 子樹同理
        from collections import deque
        q = deque()
        q.append([root, float('-inf'), float('inf')]) # node, max, min

        while q:
            node, low, high = q.popleft()

            # 1. 先檢查當前節點有沒有越界
            if node.val <= low or node.val >= high:
                return False

            if node.left:
                # 往左走：下限不變，上限縮小為當前節點的值 (high 變成 node.val)
                q.append((node.left, low, node.val))

            if node.right:
                # 往右走：上限不變，下限放大為當前節點的值 (low 變成 node.val)
                q.append((node.right, node.val, high))
        return True

            
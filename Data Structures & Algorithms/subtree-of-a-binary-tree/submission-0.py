# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def compare(p, q):
            dq = deque()
            dq.append((p, q))
            while dq:
                L, R = dq.popleft()
                # 如果兩個都沒有就是 最後一個節點 直接跳過
                if not L and not R:
                    continue
                # 比較是否有子節點 或者是否當前數值相等
                if not L or not R or L.val != R.val:
                    return False
                dq.append((L.left, R.left))
                dq.append((L.right, R.right))
            return True

        # 先找到root ＆ sub root 相同的val
        if not subRoot:
            return True

        # 然後再開始比對node
        from collections import deque
        dq = deque()
        dq.append(root)

        while dq:
            node = dq.popleft()
            if not node:
                continue
            if node.val == subRoot.val:
                if compare(node, subRoot):
                    return True
            dq.append(node.left)
            dq.append(node.right)

                
        return False


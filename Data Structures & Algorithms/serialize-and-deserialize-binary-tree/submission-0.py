# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    from collections import deque

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        q = deque()
        q.append(root)
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('N')
        # 移除最後一層Ｎ
        while res and res[-1] == 'N':
            res.pop()
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        # 把切開後的節點值，直接轉成 deque 佇列
        vals = deque(data.split(','))

        root = TreeNode(int(vals.popleft()))
        q = deque()
        q.append(root)
        while q and vals:
            node = q.popleft()
            # left side
            if vals:
                n = vals.popleft()
                if n != 'N':
                    node.left = TreeNode(int(n))
                    q.append(node.left)
            # right side
            if vals:
                n = vals.popleft()
                if n != 'N':
                    node.right = TreeNode(int(n))
                    q.append(node.right)
        return root
        
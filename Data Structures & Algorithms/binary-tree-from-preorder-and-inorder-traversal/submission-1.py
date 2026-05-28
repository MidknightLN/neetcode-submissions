# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder or not inorder:
                return None
            
            root = TreeNode(preorder[0])
            curr = root
            mid = inorder.index(preorder[0])
            # preorder 的第一個代表root
            # inorder的 左邊代表left 右邊代表right (以mid 為基準)
            curr.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
            curr.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
            return root

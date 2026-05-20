"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}
        dummy = new_head = Node(0)
        old_head = head
        while old_head:
            # 新的node
            curr = Node(old_head.val)
            # 舊的對應到新的 查表用
            seen[old_head] = curr
            # 鏈結
            new_head.next = curr
            # 更新下一個節點
            old_head = old_head.next
            new_head = new_head.next

        # 到這邊新的node中所有的鏈結已經完成 再來開始找
        while head:
            if head.random:
                curr = seen[head]
                curr.random = seen[head.random]
            head = head.next
        
        return dummy.next
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            if slow.val == fast.val:
                return True
            slow = slow.next
            fast = fast.next.next

            
        return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(0)
        val = 0

        while l1 or l2 or val:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val += v1 + v2
            head.next = ListNode(val%10)
            val = val // 10

            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

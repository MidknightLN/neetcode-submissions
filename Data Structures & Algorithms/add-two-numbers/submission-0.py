# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = head = ListNode(0)
        res = 0
        while l1 and l2:
            res = res + l1.val + l2.val
            curr = ListNode(res%10)
            res = res // 10
            head.next = curr
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            res = res + l1.val
            curr = ListNode(res%10)
            res = res // 10
            head.next = curr
            head = head.next
            l1 = l1.next
        
        while l2:
            res = res + l2.val
            curr = ListNode(res%10)
            res = res // 10
            head.next = curr
            head = head.next
            l2 = l2.next

        while res > 0:
            curr = ListNode(res%10)
            res = res // 10
            head.next = curr


        return dummy.next

        
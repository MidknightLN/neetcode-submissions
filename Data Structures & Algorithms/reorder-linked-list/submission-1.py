# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 先用快慢指針找到中間 然後reverse 後半段 最後 merge

        ## 快慢指針
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 當fast 到尾端的時候　slow 剛好會到中間 他的下一個就是 第二段的頭
        second = slow.next
        slow.next = None ## 把兩邊切斷
        
        ## reverse 後半段
        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # 當 prev 到尾端的時候 就剛好會是後半段的"頭"

        ## Merge  >> 也就是merge "head" 跟 "prev"
        dummy = newhead = ListNode()
        while head and prev:
            newhead.next = head
            head = head.next
            newhead = newhead.next
            newhead.next = prev
            prev = prev.next
            newhead = newhead.next
        if head:
            newhead.next = head
            head = head.next
            newhead = newhead.next
        if prev:
            newhead.next = prev
            prev = prev.next
            newhead = newhead.next
        
        head = dummy.next

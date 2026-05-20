# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 安全檢查：若輸入為空，直接回傳 None
        if not lists:
            return None
        # 一次兩個兩個處理
        def merge2(l1, l2):
            dummy = head = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    head = head.next
                    l1 = l1.next
                else:
                    head.next = l2
                    head = head.next
                    l2 = l2.next                  
            head.next = l1 or l2
            return dummy.next

        # Main function
        interval = 1
        amount = len(lists)
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                # 兩兩一組進行合併，並將結果直接覆蓋回原本的 lists 中
                lists[i] = merge2(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0]
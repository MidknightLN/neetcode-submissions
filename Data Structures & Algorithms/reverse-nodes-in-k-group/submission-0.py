# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 先判斷是否有足夠長度的node 切斷
        def Kstep(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        gPrev = dummy = ListNode(0, head) # 先保留一個dummy準備回傳用，gPrev 用來修改
        
        while True:
            # 先移動k步 如果是 None 就代表 走到尾端了
            curr = Kstep(gPrev, k)
            if not curr:
                break
            
            # reverse 
            nxt = curr.next  # 這個node是紀錄 下一個的起點 之後還要接上

            prev = None
            p = gPrev.next # 先把原本的頭接到新的頭上面

            while p != nxt:
                tmp = p.next
                p.next = prev
                prev = p
                p = tmp
                
            tail = gPrev.next   # 先把這個舊頭部（新尾巴）存起來
            tail.next = nxt     # 尾巴接上下一組的起點 nxt
            gPrev.next = prev   # 上一組的尾巴接上這一組的新頭部 prev
            
            gPrev = tail        # 把 gPrev 移動到這組的尾巴，準備下一輪
            
        return dummy.next

                
    


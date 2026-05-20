class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 小優化
        if not nums or k == 0:
            return []
        # 使用deque做雙端隊列
        from collections import deque
        q = deque()
        res = []
        # 先將window 擴張到k
        for i in range(k):
            # 淘汰小於 目前數值的 元素
            while q and q[-1][1] < nums[i]:
                q.pop()
            # 加入當前元素
            q.append((i, nums[i]))
        res.append(q[0][1])

        # 真正開始 slide
        for i in range(k, len(nums)):
            # 檢查頭部是否過期需要移除
            if q[0][0] == i - k:
                q.popleft()

            # 淘汰小於 目前數值的 元素
            while q and q[-1][1] < nums[i]:
                q.pop()
            # 加入當前元素
            q.append((i, nums[i]))
            
            # 記錄答案
            res.append(q[0][1])
        return res
        


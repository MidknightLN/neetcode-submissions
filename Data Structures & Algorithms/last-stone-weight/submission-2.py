class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = [-s for s in stones]
        import heapq
        heapq.heapify(hq) # 存負數進去

        while len(hq) > 1:
            val1 = heapq.heappop(hq)
            val2 = heapq.heappop(hq)

            if val1 == val2:
                continue
            else:
                heapq.heappush(hq, val1-val2)
        
        if len(hq) == 0:
            return 0
        else:
            return -(heapq.heappop(hq))
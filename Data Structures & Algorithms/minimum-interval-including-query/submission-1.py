class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # two pointer + min heap

        # 1. 将区间按照起点从小到大排序
        intervals.sort(key=lambda x: x[0])
        # 2. 去重複 然後從小到大排序
        requeries = sorted(list(set(queries)))
        # 這個用來存 查到的最小數值
        ordermap = defaultdict(int)

        n = len(intervals)
        min_heap = []
        idx = 0
        for q in requeries:
            # 起點小於要求的放入
            while idx < n and intervals[idx][0] <= q:
                # 因為這題要求的是「最小的區間長度」。我們把 r - l + 1 放在第一個位置，
                # 就是為了強迫 Heap 以「長度最小」為第一優先進行排序。
                length = intervals[idx][1] - intervals[idx][0] + 1
                end_point = intervals[idx][1]
                heapq.heappush(min_heap, (length, end_point))
                idx += 1
            # 終點小於要求的代表沒包含到 >> 剔除
            # 如果有包含到，也就代表 他是最短的有效答案，後續的不用管。
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # 紀錄答案
            if min_heap:
                ordermap[q] = min_heap[0][0] # 堆頂的長度
            else:
                ordermap[q] = -1 
        
        return [ordermap[q] for q in queries]
            




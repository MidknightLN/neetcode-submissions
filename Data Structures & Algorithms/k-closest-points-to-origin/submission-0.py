class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        max_heap = []
        
        for x, y in points:
            # 1. 計算歐幾里得距離的平方（免去開根號以保持精準度與速度）
            # 距離公式：x^2 + y^2
            dist = x**2 + y**2
            
            # 2. 因為要 Max-Heap，權重丟負的：(-dist, [x, y])
            heapq.heappush(max_heap, (-dist, [x, y]))
            
            # 3. 如果 Heap 超過 K 個元素，把最遠的（頂端最大的負數）踢掉
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # 4. 最後 max_heap 留下來的剛好就是最近的 K 個點，把座標撈出來
        return [point for dist, point in max_heap]
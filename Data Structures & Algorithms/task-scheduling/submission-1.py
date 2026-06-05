class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # 先統計每個字元出現得次數
        from collections import Counter
        counts = Counter(tasks)
        # 我們只需要消耗次數，不需要管任務名稱是 A 還是 B
        # 從最大的開始看 所以 要彈出的是最大的  轉負數 可以讓最大的在頂端
        import heapq
        max_heap = [ -num  for num in counts.values()]
        heapq.heapify(max_heap)

        # 從heap 開始看 每次彈出 放到queue中 並且記錄下次放回heap的時間
        from collections import deque
        cd_queue = deque()
        time = 0
        # 開始跑
        while max_heap or cd_queue:
            time += 1
            if max_heap:
                val = heapq.heappop(max_heap)
                val += 1 # 特別注意 這邊是負數 剩餘次數歸零要用加法
                if val < 0:
                    cd_queue.append([time+n, val])
            if cd_queue and cd_queue[0][0] == time:
                _, remain = cd_queue.popleft()
                heapq.heappush(max_heap, remain)
        return time


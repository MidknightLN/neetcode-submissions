class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 起點找終點： 二分法一邊找一邊就把「重疊條件」當作搜尋的濾網，出了二分法後，你就直接得到答案了。

        n = len(intervals)

        # 先找開頭>>第一個覆蓋的區間 (左閉右開)
        l, r  = 0, n
        while l < r:
            mid = l + (r-l)//2
            if newInterval[0] <= intervals[mid][1]:
                # 重疊區域可能在right 當下的區間內
                r = mid  
            else:
                # 重疊區域一定 不在left 包含的區間內（因為是終點）
                l = mid+1  
        leftIndex = l

        # 找結尾重疊>> 第一個沒有覆蓋的區間 (左閉右開)
        l, r  = 0, n
        while l < r:
            mid = l + (r-l)//2
            if newInterval[1] < intervals[mid][0]:
                # 重疊區域可能在right 往前一個的區間內
                r = mid
            else:
                # 重疊區域可能在left 包含的區間內
                l = mid+1
        rightIndex = l - 1

        # 情況 A：有重疊，需要合併 (leftIndex <= rightIndex)
        if leftIndex <= rightIndex:
            start = min(newInterval[0], intervals[leftIndex][0])
            end = max(newInterval[1], intervals[rightIndex][1])
            return intervals[:leftIndex] + [[start, end]] + intervals[rightIndex + 1:]
            # 情況 B：沒重疊，純插入 (leftIndex > rightIndex)
        else:
            return intervals[:leftIndex] + [newInterval] + intervals[leftIndex:]

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        max_reached = intervals[0][0]

        for start, end in intervals:
            if start >= max_reached:
                max_reached = end
            else:
                res += 1
                max_reached = min(end, max_reached)
        return res
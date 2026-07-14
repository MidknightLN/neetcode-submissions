class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        dp = [float('inf') for _ in range(10001)]

        for region in intervals:
            l = region[1] - region[0] +1
            for idx in range(region[0], region[1]+1):
                dp[idx] = min(dp[idx], l)
        res = []
        for q in queries:
            if dp[q] == float('inf'):
                res.append(-1)
            else:
                res.append(dp[q])
        return res
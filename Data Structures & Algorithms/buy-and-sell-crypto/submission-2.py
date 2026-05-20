class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        # slide windows
        while r < len(prices):
            # 如果當前價格較高就嘗試賣出
            if prices[l] < prices[r]:
                # 計算獲利
                max_profit = max(max_profit, prices[r] - prices[l])
            # 如果當前價格更低就嘗試從這一天買入
            else:
                l = r
            # 更新 右側 邊界
            r += 1

        return max_profit
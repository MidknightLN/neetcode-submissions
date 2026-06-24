class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化 DP 陣列，因為求最小值，所以預設為無限大 (float('inf'))
        # 陣列長度為 amount + 1，因為要包含金額 0 到 amount
        dp = [float('inf') for _ in range(amount+1)]
        # 基礎狀態：湊齊金額 0 需要 0 枚硬幣
        dp[0] = 0
        
        # 外層迴圈：依序計算金額 1 到 amount 的最少硬幣數
        for i in range(1, amount + 1):
            # 內層迴圈：嘗試每一種硬幣
            for coin in coins:
                # 只有當目前金額大於等於硬幣面額時，才能選擇這枚硬幣
                if i >= coin:
                    # 轉移方程式：不拿這枚硬幣 vs 拿了這枚硬幣(dp[i-coin] 再加 1 枚)
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return  dp[amount] if dp[amount] != float('inf') else -1
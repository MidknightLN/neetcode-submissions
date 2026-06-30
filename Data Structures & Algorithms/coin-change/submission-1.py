class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 假設有一元硬幣也只需要 amount 個 所以 (amount + 1) 用來代表不可能到達的數字
        dp = [(amount + 1) for _ in range(amount + 1)]
        dp[0] = 0

        for amt in range(amount + 1):
            for c in coins:
                # 如果"剩下需要補的數量" 扣掉硬幣還>=0
                if amt - c >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
        
        return dp[amount] if dp[amount] != (amount + 1) else -1

                
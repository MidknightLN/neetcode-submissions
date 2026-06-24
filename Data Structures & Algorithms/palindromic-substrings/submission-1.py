class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        res = 0
        # 設定基礎判斷1 奇數
        for i in range(n):
            dp[i][i] = True
            res += 1

        # 設定基礎判斷2 偶數
        for i in range(n-1):
            # 必須確保 i 至少是 1，才有前一個字元可以比
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
        
        # 開始狀態轉移
        for i in range(n-1, -1, -1):
            for j in range(i+2, n):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res += 1
        return res 


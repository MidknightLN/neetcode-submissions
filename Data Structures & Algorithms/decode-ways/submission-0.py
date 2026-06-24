class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0 for _ in range(n+1)]

        # 設定初始狀態
        dp[0] = 1 # 這個代表 “不選第一個字來解” >> 已解碼的字串＝“”
        dp[1] = 1 # 這個代表 把第一個字元拿來解碼  ## 附註 前面已經排除0

        # dp[2] >> 
        for i in range(2, n+1):
            # 先判斷是否可以正常組合
            # 1. 檢查最後 1 位數 (對應的字元索引是 s[i-1])
            one_digit = s[i-1]
            if '1' <= one_digit <= '9':
                dp[i] += dp[i-1]
                
            # 2. 檢查最後 2 位數 (對應的字元區間是 s[i-2:i])
            two_digits = s[i-2:i]
            if "10" <= two_digits <= "26":
                dp[i] += dp[i-2]
        
        return dp[n]
        
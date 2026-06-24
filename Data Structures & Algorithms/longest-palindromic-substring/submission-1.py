class Solution:
    # 最長的 回文
    def longestPalindrome(self, s: str) -> str:
        # 單一一個字元的 時候 必定是 回文
        n = len(s)
        if n < 2:
            return s

        # 紀錄答案
        max_len = 1
        start_idx = 0
        # 建立狀態轉移 >> dp[i][j] 代表 字串從 i到j 是否是回文
        # 長字串由短字串轉移而來 >> 左右分別各內縮一個字元 >> dp[i+1][j-1] >> 左下角
        dp = [[False for _ in range(n)] for _ in range(n)]

        # 1. 預設判斷一：所有長度 1 的子字串 (對角線)
        for i in range(n):
            dp[i][i] = True
            
        # 2. 預設判斷二：所有長度 2 的子字串 (偶數基礎)
        # 這樣就徹底解決了偶數長度內縮會「越界到左下角」的問題
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                start_idx = i

        # 開始狀態轉移 ＃從左到右 從下到上 >> 只需要算右上角三角形
        for i  in range(n-1, -1, -1):
            for j in range(i+1, n):
                # 核心判定：頭尾字元要相同 並且子字串狀態為Ture
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        start_idx = i

        return s[start_idx:start_idx+max_len]

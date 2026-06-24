class Solution:
    # 最長的 回文
    def longestPalindrome(self, s: str) -> str:
        # 單一一個字元的 時候 必定是 回文
        n = len(s)
        if n < 2:
            return s

        # 建立狀態轉移 >> dp[i][j] 代表 字串從 i到j 是否是回文
        # 長字串由短字串轉移而來 >> 左右分別各內縮一個字元 >> dp[i+1][j-1] >> 左下角
        dp = [[False for _ in range(n)] for _ in range(n)]

        # 每個單一字元都是回文 (對角線)
        for i in range(n):
            dp[i][i] = True
        
        # 紀錄答案
        max_len = 1
        start_idx = 0
        # 開始狀態轉移 ＃從左到右 從下到上 >> 只需要算右上角三角形
        for i  in range(n-1, -1, -1):
            for j in range(i+1, n):
                # 核心判定：頭尾字元要相同 並且子字串狀態為Ture
                if s[i] == s[j]:
                    # 如果長度 <= 3 (即 j-i <= 2)，不用查左下角，直接是 True
                    # 如果長度 > 3，才需要確保左下角 dp[i+1][j-1] 也是 True
                    if j - i <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True

                        if j-i+1 > max_len:
                            max_len = j-i+1
                            start_idx = i

        return s[start_idx:start_idx+max_len]

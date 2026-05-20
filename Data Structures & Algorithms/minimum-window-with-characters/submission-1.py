class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # 先存 目標t應該有的數值
        seen = defaultdict(int)
        for c in t:
            seen[c] += 1
        # 這個東西代表有多少要找的字元
        len_t = len(t)

        # 優化起點
        l, r = -1, -1
        for idx, c in enumerate(s):
            if c in seen:
                l, r = idx, idx
                break
        if l == -1:
            return ""
        
        # 開始查找
        res = (0, float('inf'))
        while r < len(s):
            # 如果他是我們在意的字元
            if s[r] in seen:
                # 檢查是否是我們真正需要的
                if seen[s[r]] > 0:
                    len_t -= 1
                seen[s[r]] -= 1
            r += 1
            # 收縮階段
            while len_t == 0:
                # 更新歷史最短的邊界（Tuple 比較長度）
                if (r - l) < (res[1] - res[0]):
                    res = (l, r)
                # 開始刪減
                if s[l] in seen:
                    seen[s[l]] += 1
                    # 檢查是否是我們真正需要的
                    if seen[s[l]] > 0:
                        len_t += 1
                l += 1
        if res[1] == float('inf'):
            return ""
        else:
            return s[res[0]:res[1]]

                    
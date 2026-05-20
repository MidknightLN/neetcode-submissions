class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 擴張(直到滿足條件） >> 收縮(嘗試縮小直到不滿足條件) >> 計算結果

        # 如果沒有字元
        if not s or not t or len(s) < len(t):
            return ""

        seen = defaultdict(int)
        # 把目標字元存到seen 裡面   len_t 代表真正需要的字元目前有幾個了
        for c in t:
            seen[c] += 1
        len_t = len(t)

        l, r = -1, -1
        # 先找到第一個在 t 裡面的字元 ，如果前面都沒出現 這些字元也是不需要的
        for idx, c in enumerate(s):
            if c in t:
                l, r = idx, idx
                break
        if l == -1:
            return ""
        
        res = (-1, len(s)) # 記錄最短答案 (left index, right index)
        
        # 直到觸及邊界之前都要一直看 # 從idx 開始擴張slide window
        while r < len(s):
            if s[r] in seen:
                if seen[s[r]] > 0:
                    len_t -= 1
                seen[s[r]] -= 1
            r += 1
            
            # 收縮左window
            while len_t == 0:
                # 更新歷史最短的邊界（Tuple 比較長度）
                if (r - l) < (res[1] - res[0]):
                    res = (l, r)
                
                if s[l] in seen:
                    seen[s[l]] += 1
                    if seen[s[l]] > 0:
                        len_t += 1

                l += 1

        return s[res[0]:res[1]] if res[0] != -1 else ""



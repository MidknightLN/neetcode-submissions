class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = [0 for _ in range(26)]
        # 先把s1 放入
        for c in s1:
            val = ord(c) - ord('a')
            seen[val] -= 1
        window = len(s1)
        l, r = 0, 0
        while r < len(s2):
            if r - l  < window:
                val = ord(s2[r]) - ord('a')
                seen[val] += 1
                r += 1
            else:
                if seen.count(0) == 26:
                    return True
                else:
                    val = ord(s2[l]) - ord('a')
                    seen[val] -= 1
                    l += 1
                    val = ord(s2[r]) - ord('a')
                    seen[val] += 1
                    r += 1
        return True if seen.count(0) == 26 else False


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_l = 0
        seen = defaultdict(int)
        while r < len(s):
            val = ord(s[r]) - ord('a')
            if seen[val] == 0:
                seen[val] = 1
                r += 1
                max_l = max(max_l, r - l)
            else:
                val = ord(s[l]) - ord('a')
                seen[val] -= 1
                l += 1
        return max_l
                
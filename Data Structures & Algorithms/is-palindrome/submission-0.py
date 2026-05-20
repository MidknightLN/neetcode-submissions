class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 回文 
        # 移除所有空格以及非目標字元
        # 然後用兩個pointer 比對
        # Space: O(1)
        # Time: O(n)
        def check(c):
            if (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
                return True
            return False

        l, r = 0, len(s)-1

        while l < r:
            if not check(s[l]):
                l += 1
                continue
            if not check(s[r]):
                r -= 1
                continue
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
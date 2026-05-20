class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        seen = {']':'[', '}':'{', ')':'('}
        l, r = 0, len(s)

        while l < r:
            if s[l] in {'[', '{', '('}:
                stack.append(s[l])
                l += 1
                continue

            if (not stack) or (seen[s[l]] != stack.pop()):
                return False
            else:
                l += 1
        return True if not stack else False


        
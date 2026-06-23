class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import cache
        @cache
        def dp(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            
            return dp(n-1) + dp(n-2)
        
        return dp(n)

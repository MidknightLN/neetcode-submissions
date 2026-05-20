class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r-l)//2
            res = 0
            for p in piles:
                # (a + b - 1) // b
                # -(-a // b)
                # math.ceil()
                res += (p + mid - 1) // mid
            if res > h:
                l = mid + 1
            else:
                r = mid - 1
        return l
            

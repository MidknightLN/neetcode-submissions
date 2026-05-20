class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 速度最慢是 1（每小時吃 1 根），最快是 max(piles)（每小時直接吃完最大的一堆）
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r-l)//2
            res = 0
            for p in piles:
                # 以下三種都可以達到目標，無條件進位
                # (a + b - 1) // b
                # -(-a // b)
                # math.ceil()
                res += (p + mid - 1) // mid
            if res > h:
                l = mid + 1
            else:
                # 如果 res <= h，代表這個速度可以準時吃完（是個合法答案）
                # 但為了找「最小」速度，我們讓右界往左縮，繼續逼近極限！
                r = mid - 1
        # 根據雙閉區間退出時的特性：
        # 當迴圈結束時，l 會剛好停在「第一個滿足條件（res <= h）」的最小速度上
        return l
            

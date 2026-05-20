class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer
        l, r = 0, len(height) -1
        res = 0
        lh_max, rh_max = height[l], height[r]
        while l < r:
            # 核心邏輯：哪邊的牆短，就從哪邊往中間推進
            if  lh_max < rh_max:
                l += 1
                lh_max = max(lh_max, height[l])
                res += lh_max - height[l]
            else:
                r -= 1
                rh_max = max(rh_max, height[r])
                res += rh_max - height[r]
        return res
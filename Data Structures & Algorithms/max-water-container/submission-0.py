class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if  heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return res


        # two pointer
        # l, r = 0, len(heights) -1
        # res = 0
        # lh_max, rh_max = heights[l], heights[r]
        # while l < r:
        #     # 核心邏輯：哪邊的牆短，就從哪邊往中間推進
        #     if  lh_max < rh_max:
        #         l += 1
        #         lh_max = max(lh_max, heights[l])
        #         res += lh_max - heights[l]
        #     else:
        #         r -= 1
        #         rh_max = max(rh_max, heights[r])
        #         res += rh_max - heights[r]
        # return res

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        step = 1
        l = 0
        r = nums[0]

        while r < len(nums) -1:
            max_reached = 0
            for idx in range(l, r+1):
                max_reached = max(max_reached, idx + nums[idx])
            l = r+1
            r = max_reached
            step += 1
        return step





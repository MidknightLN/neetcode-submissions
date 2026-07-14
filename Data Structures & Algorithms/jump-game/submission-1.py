class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reached = 0

        for idx in range(len(nums)):
            if max_reached < idx:
                return False
            elif max_reached >= len(nums)-1:
                return True
            max_reached = max(max_reached, idx + nums[idx])
        return True
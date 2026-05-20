class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        # 出來後 r= 轉換點 >> 最小值
        if nums[-1] >= target >= nums[r]:
            l, r = r, len(nums)-1
        elif nums[0] <= target <= nums[r-1]:
            l, r = 0, r - 1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time: O(log N) 

        # 「右界減一（len-1），要帶（l <= r），
        # 左右鄰居挪一格（mid + 1 / mid - 1）。」

        # 雙閉區間 = 精準數值 唯一目標
        # 左閉右開 = 符合條件的第一個數值
        l, r = 0, len(nums) -1

        while l <= r:
            mid = l + (r - l) // 2
            print( l, mid , r)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
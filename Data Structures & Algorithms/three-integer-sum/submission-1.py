class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l, r = 0, len(nums)-1 
        res = []
        while l < r - 1 :
            # 如果當前數字大於 0，後面的和一定大於 0（優化）
            if nums[l] > 0:
                break
            # 如果目前taeget 跟上次重複 就跳過
            if l > 0 and nums[l] == nums[l-1]:
                l += 1
                continue
            # 開始找後面兩個數字
            temp_l = l + 1
            temp_r = r
            while temp_l < temp_r:
                total = nums[l] + nums[temp_l] + nums[temp_r] 

                if total > 0:
                    temp_r -= 1
                elif total < 0:
                    temp_l += 1
                elif total == 0:
                    res.append([nums[l], nums[temp_l], nums[temp_r]])
                    temp_l += 1
                    temp_r -= 1
                    # 找到解後，如果數值跟原本一樣就跳過
                    while temp_l < temp_r and nums[temp_l] == nums[temp_l - 1]:
                        temp_l += 1
                    while temp_l < temp_r and nums[temp_r] == nums[temp_r + 1]:
                        temp_r -= 1
                    
            l += 1
        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 利用了前一個子問題的局部最優解 >> 到I-1個的最大數值以及最小數值。
        res = max(nums)
        currMax = 1 # 任何數字乘1都不改變
        currMin = 1

        for n in nums:
            if n == 0: # 遇到0的時候先還原 直接看後面的
                currMax = 1
                currMin = 1
                continue
            # 防止重複計算 所以用TEMP 存
            tempMax = currMax*n
            tempMin = currMin*n
            # 開始比較 因為負負得正的關係 所以才需要存三個並且比較 
            currMax = max(tempMax, tempMin, n)
            currMin = min(tempMax, tempMin, n)
            # 最後只需要比較最大數字 因此不用比MIN
            res = max(res, currMax)
        return res
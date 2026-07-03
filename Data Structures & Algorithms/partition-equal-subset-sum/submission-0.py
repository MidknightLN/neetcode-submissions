class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 問題要求：分成兩個子集合 加總相等

        # 怕重複就倒著走（從大到小），想重複就正著走（從小到大）
        
        # 如果數列是奇數 代表不可能正常分成兩份。
        if sum(nums) %2 == 1:
            return False 
        # 目標數值為一半
        target = sum(nums)//2

        # dp 的索引代表「目標總和」，所以要開 target + 1 個格子
        dp = [False for _ in range(target + 1)]
        dp[0] = True  # 背包容量 0 絕對做得出來

        # 外層迴圈：一個一個數字拿出來放進背包
        for num in nums:
            # 內層迴圈：怕重複就倒著走（從大到小）
            # 從 target 倒著算回 num。低於 num 的容量根本放不下 num，所以不用算。
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                
            # 💡 剪枝小優化：如果目標值已經被湊出來了，後面不用看了，直接提早收工！
            if dp[target]:
                return True
        return False
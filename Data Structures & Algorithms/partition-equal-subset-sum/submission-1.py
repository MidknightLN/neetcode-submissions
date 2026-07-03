class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 問題要求：分成兩個子集合 加總相等
        
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
            # 創建一個 Queue (或 List) 來記錄這一輪「新點亮」的格子
            new_trues = []
            # 從小到大正著走
            for i in range(target + 1):
                # 看到以前有 True，且加上 num 後不會超出邊界
                if dp[i] and i + num <= target:
                    # 我們不直接修改 dp[i + num]，而是先丟進 Queue 裡！
                    new_trues.append(i + num)
                    
            # 這一輪所有格子都看完了，再把 Queue 裡的新燈泡全部點亮
            for position in new_trues:
                dp[position] = True
            if dp[target] == True:
                return True
                    
        return False
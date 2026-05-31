class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        for n in nums:
            # 對於目前 res 中的每一個子集 curr，都建立一個包含 n 的「全新清單」
            # curr + [n] 會在記憶體中產生新的物件，不會有共用參照的問題
            res += [curr + [n] for curr in res]
        
        return res
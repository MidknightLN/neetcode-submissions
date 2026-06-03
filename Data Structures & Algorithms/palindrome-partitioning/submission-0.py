class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def vali_pali(s):
            return s == s[::-1]

        subset = []
        def backtracking(index): # index = 使用的總字串
            # 每次選擇從哪邊切刀 切下來前半段判斷是否是 回文 後半段繼續丟到下一次判斷
            # 不符合的時候退回
            # 
            if index == len(s):
                res.append(subset[:])
                return 
            # 在加入的時候 先驗證
            for end in range(index, len(s)):
                if vali_pali(s[index:end+1]):
                    subset.append(s[index:end+1])
                    backtracking(end+1)
                    subset.pop()
            
        backtracking(0)
        return res


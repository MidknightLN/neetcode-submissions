class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #利用前一個子問題的局部最優解


        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        wordSet = set(wordDict)

        for idx in range(1, len(s)+1):
            for i in range(idx):
                if dp[i] and s[i:idx] in wordSet:
                    dp[idx] = True
                    break
        return dp[len(s)]
            
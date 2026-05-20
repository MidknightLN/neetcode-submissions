class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## (idx, temperature)
        stack = []
        res = [0 for _ in range(len(temperatures))]
        l, r = 0, len(temperatures) 

        while l < r :
            while stack and stack[-1][1] < temperatures[l]:
                (idx, t) = stack.pop()
                res[idx] = l - idx
            stack.append((l, temperatures[l]))
            l+=1
        return res


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 注意 回傳的是index 並且從1開始
        # visited = defaultdict(int)
        # for idx, val in enumerate(numbers):
        #     if visited.get(val):
        #         return [visited[val], idx+1]
        #     else:
        #         visited[target - val] = idx+1

        # 因為題目要求使用Space: O(1)
        # 改使用 two pointer
        l, r = 0, len(numbers) -1

        while l < r:
            curr = numbers[l]+numbers[r] 
            if curr == target:
                return [l+1, r+1]
            elif curr > target:
                r -= 1
            else:
                l += 1
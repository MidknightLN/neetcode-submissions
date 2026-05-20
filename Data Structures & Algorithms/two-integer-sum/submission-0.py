class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = defaultdict(int)
        for idx, num in enumerate(nums):
            if num in visited:
                return [visited[num], idx]
            visited[target - num] = idx
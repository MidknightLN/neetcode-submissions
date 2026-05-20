class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        visited = defaultdict(int)

        for num in nums:
            if visited[num] != 0:
                return True
            visited[num] = 1
        
        return False